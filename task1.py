from utils.loader import load_ontology, load_model

g = load_ontology("Ontologies/Cartoon/Cartoon.ttl")
model = load_model()

intro = "Our project aims to develop a system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs)"
query = "Ontology Hierarchy Validation: Generate all the subclass- superclass structures, and ensure the subclass-superclass relationships are correctly structured"

q = intro +"Given this ontology in a turtle file " +  g.serialize(format="turtle") +  "Perform this task and give appropriate solution: " + query
response1 = model.generate_content(q)

print("Superclass Subclass Heirarchy Identified within the ontology")
print(response1.text)
prompt = "For every superclass, generate a list of possible subclasses in the following response: "+response1.text +". If there are n super classes, then there must be n lists for sub classes."
response2 = model.generate_content(prompt)

print("List of possible subclasses for each superclass identified by the LLM")
print(response2.text)

prompt2 =  "Validate whether the subclasses identified in" + response2.text + "  include the following subclasses: " + response1.text +". Enlist the validated subclasses as well."
response3 = model.generate_content(prompt2)

print("Validated subclasses: ")
print(response3.text)

