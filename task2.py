from utils.loader import load_ontology, load_model
from sentence_transformers import SentenceTransformer

# model_2 = SentenceTransformer('all-mpnet-base-v2')

g = load_ontology("class_ttls/SportsTeam.ttl")
model = load_model()

intro = "Our project aims to develop a system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs)"
query = "Property Domain/Range Validation: Identify all the relationships and properties in this ttl file, with their domain and range"

q = intro +"Given this ontology in a turtle file " +  g.serialize(format="turtle") +  "Perform this task and give appropriate solution: " + query
response1 = model.generate_content(q)

print("Properties Identified within the ontology")
print(response1.text)

prompt = "For every property identified, generate a list of possible domain and range in the following response: "+response1.text +". If there are n properties, then there must be n lists for domain and range."
response2 = model.generate_content(prompt)

print("List of possible domain and range for the properties")
print(response2.text)

prompt2 =  "Validate whether the domain and range identified in" + response2.text + "  include the following domain and range: " + response1.text +". Enlist the validated properties as well."
response3 = model.generate_content(prompt2)

print("Validated properties: ")
print(response3.text)

