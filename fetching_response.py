from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef
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

# Post-processing
ontology_classes = []
for result in results["results"]["bindings"]:
    class_uri = result["class"]["value"]
    if class_uri.startswith("http://dbpedia.org/ontology/"):
        ontology_classes.append(class_uri)

# Run a query for each ontology class
for ontology_class in ontology_classes:
    sparql.setQuery(f"""
        SELECT ?subject ?predicate ?object WHERE {{
          ?subject rdf:type <{ontology_class}> .
          ?subject ?predicate ?object .
        }}
        LIMIT 100
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Create a new RDF graph
    g = Graph()

    # Add triples to the graph
    for result in results["results"]["bindings"]:
        subject = URIRef(result["subject"]["value"])
        predicate = URIRef(result["predicate"]["value"])
        object = URIRef(result["object"]["value"])
        g.add((subject, predicate, object))

    # Create a subfolder for the ontology class
    ontology_name = ontology_class.split("/")[-1]
    os.makedirs("Ontologies/"+ontology_name, exist_ok=True)

    # Save the graph to a ttl file in the subfolder
    with open(f"Ontologies/{ontology_name}/{ontology_name}.ttl", "wb") as f:
        f.write(g.serialize(format="turtle").encode('utf-8'))
    # Print results
    for result in results["results"]["bindings"]:
        print(result["subject"]["value"], result["predicate"]["value"], result["object"]["value"])
