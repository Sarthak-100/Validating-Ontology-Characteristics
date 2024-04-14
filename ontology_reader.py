from rdflib import Graph

def load_ontology(ontology_url):
    # Create a new graph
    g = Graph()

    # Parse the ontology from the given URL
    g.parse(ontology_url,format="turtle")

    return g

# Usage
g = load_ontology("output3.ttl")
# g.serialize(format="turtle", destination="output3.ttl")
print(g.serialize(format="turtle"))

# for s,p,o in g:
#     print(s,p,o)