from SPARQLWrapper import SPARQLWrapper, JSON
import os

sparql = SPARQLWrapper("https://dbpedia.org/sparql")

# Fetch distinct classes from DBpedia
sparql.setQuery("""
    SELECT DISTINCT ?class WHERE {
      [] a ?class .
    }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(".....Done Fetching Class Names")

# Post-processing
ontology_classes = []
for result in results["results"]["bindings"]:
    class_uri = result["class"]["value"]
    if class_uri.startswith("http://dbpedia.org/ontology/"):
        ontology_classes.append(class_uri)

print(".....Filtered Classes with DBPedia Ontology URI Prefix")

def fetch_subproperties(property_uri):
    subproperties = []
    sparql.setQuery(f"""
        SELECT DISTINCT ?subproperty WHERE {{
            ?subproperty rdfs:subPropertyOf <{property_uri}> .
        }}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        subproperty_uri = result["subproperty"]["value"]
        subproperties.append(subproperty_uri)
    return subproperties

def fetch_properties_and_save(class_uri):
    try:
        decoded_class_uri = class_uri.replace(" ", "_")
        sparql.setQuery(f"""
            SELECT DISTINCT ?property WHERE {{
                ?subject rdf:type <{decoded_class_uri}> ;
                        ?property [] .
                OPTIONAL {{
                    ?property rdfs:subPropertyOf [] .
                }}
            }}
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # Create a folder to store TTL files if it doesn't exist
        folder_name = "class_ttls_prop"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Write properties and their subproperties to a TTL file
        file_name = f"{class_uri.split('/')[-1]}.ttl"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            for result in results["results"]["bindings"]:
                property_uri = result["property"]["value"]
                f.write(f"<{property_uri}> rdf:type rdf:Property .\n")
                
                # Fetch subproperties of the property
                subproperties = fetch_subproperties(property_uri)
                for subproperty in subproperties:
                    f.write(f"<{property_uri}> rdfs:subPropertyOf <{subproperty}> .\n")
                
    except Exception as e:
        print(f"Failed to fetch properties for class: {class_uri}")

# Fetch properties for each ontology class and save to TTL files
for ontology_class_uri in ontology_classes:
    fetch_properties_and_save(ontology_class_uri)
