from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef
from urllib.parse import quote
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

# Define a function to fetch relationships/properties of a given class
def fetch_properties_for_class(class_uri):
    sparql.setQuery(f"""
        SELECT DISTINCT ?property ?domain ?range WHERE {{
          ?subject rdf:type <{class_uri}> ;
                   ?property [] .
          OPTIONAL {{
            ?property rdfs:domain ?domain .
            ?property rdfs:range ?range .
          }}
        }}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Extract properties
    properties = [result["property"]["value"] for result in results["results"]["bindings"]]

    return properties

print("Started Storing Properties for each class.....")

# Fetch properties for each ontology class
# class_properties_mapping = {}
# for ontology_class_uri in ontology_classes:
#     decoded_class_uri = quote(ontology_class_uri, safe='/:')
#     properties = fetch_properties_for_class(decoded_class_uri)
#     class_properties_mapping[ontology_class_uri] = properties

# print(".....Done Fetching Properties for each class")

# # Print the mapping of classes to their properties
# for ontology_class_uri, properties in class_properties_mapping.items():
#     print(f"Class: {ontology_class_uri}")
#     print("Properties:")
#     for prop in properties:
#         print(f"- {prop}")
#     print()

# Define a function to fetch relationships/properties of a given class and save them to a TTL file
def fetch_properties_and_save(class_uri):
    try:
        decoded_class_uri = quote(class_uri, safe='/:')
        properties = fetch_properties_for_class(decoded_class_uri)

        # Create a folder to store TTL files if it doesn't exist
        folder_name = "class_ttls"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Write properties to a TTL file
        file_name = f"{class_uri.split('/')[-1]}.ttl"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            for prop in properties:
                f.write(f"{prop}\n")
    except Exception as e:
        print(f"Failed to fetch properties for class: {class_uri}")

# Fetch properties for each ontology class and save to TTL files
for ontology_class_uri in ontology_classes:
    fetch_properties_and_save(ontology_class_uri)