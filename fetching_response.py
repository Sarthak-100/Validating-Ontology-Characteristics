from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://dbpedia.org/sparql")
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

    # Print results
    for result in results["results"]["bindings"]:
        print(result["subject"]["value"], result["predicate"]["value"], result["object"]["value"])
