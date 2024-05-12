from utils.loader import load_ontology, load_model

g = load_ontology("Ontologies/Cartoon/Cartoon.ttl")
model = load_model()

# Query for all subclasses (anything that is a type of something else)
qres = g.query(
    """
    SELECT ?subclass ?superclass
    WHERE {
      ?subclass a ?superclass .
    }
    """
)

response_txt = ""

# Create a dictionary to hold the superclasses and their subclasses
superclasses = {}
superclass_lst = ""

for row in qres:
    subclass, superclass = row
    if superclass not in superclasses:
        superclasses[superclass] = set()
    superclasses[superclass].add(subclass)

# Print the superclasses and their subclasses
for superclass, subclasses in superclasses.items():
    response_txt += f"Superclass: {superclass}\n"
    print(f"Superclass: {superclass}")
    superclass_lst+=superclass + ","
    for subclass in subclasses:
        response_txt += f" - Subclass: {subclass}\n"
        print(f" - Subclass: {subclass}")

# # print(superclass_lst)
# intro = "Our project aims to develop a system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs)."
# # query = "Ontology Hierarchy Validation: Generate all the subclass- superclass structures, and ensure the subclass-superclass relationships are correctly structured"

# # q = intro +"Given this ontology in a turtle file " +  g.serialize(format="turtle") +  "Perform this task and give appropriate solution: " + query
# # response1 = model.generate_content(q)

# # print("Superclass Subclass Heirarchy Identified within the ontology")
# # print(response1.text)

# prompt = intro + "For every identified superclass in the following text , generate a list of possible subclasses: "+ superclass_lst +". If there are n super classes, then there must be n lists for sub classes."
# response = model.generate_content(prompt)

# print("List of possible subclasses for each superclass identified by the LLM")
# print(response.text)

# # prompt2 =  "Validate whether the subclasses identified in" + response2.text + "  include the following subclasses: " + response1.text +". Enlist the validated subclasses as well."
# # response3 = model.generate_content(prompt2)

# # print("Validated subclasses: ")
# # print(response3.text)

