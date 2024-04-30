from utils.loader import load_ontology, load_model

# Load the ontology and the language model
g = load_ontology("class_ttls/SportsTeam.ttl")
model = load_model()

# Introduction and task query
intro = "Our project aims to develop a system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs)"
query = "Property Hierarchy Validation: Generate all the subproperty- superproperty structures, and ensure the subproperty- superproperty relationships are correctly structured"

# Generate the content for the task
q = intro + "Given this ontology in a turtle file " +  g.serialize(format="turtle") +  "Perform this task and give appropriate solution: " + query
response1 = model.generate_content(q)

print("Property Hierarchy Identified within the ontology")
print(response1.text)

# Generate a list of possible super-properties for each property identified
prompt = "For every property identified, generate a list of possible super-properties in the following response: "+response1.text +". If there are n properties, then there must be n lists for super-properties."
response2 = model.generate_content(prompt)

print("List of possible super-properties for each property identified by the LLM")
print(response2.text)

# Validate whether the super-properties identified include the following super-properties
prompt2 =  "Validate whether the super-properties identified in" + response2.text + "  include the following super-properties: " + response1.text +". Enlist the validated properties as well."
response3 = model.generate_content(prompt2)

print("Validated properties: ")
print(response3.text)
