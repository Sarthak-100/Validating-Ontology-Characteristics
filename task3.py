from rdflib import Graph, OWL, RDF, RDFS
from utils.loader import load_ontology, load_model

# Load the ontology and the model
g = load_ontology("class_ttls/SportsTeam.ttl")
model = load_model()

# Define the types of properties we are interested in
property_types = [OWL.SymmetricProperty, OWL.TransitiveProperty, OWL.FunctionalProperty, OWL.ReflexiveProperty]

# Initialize a dictionary to store the properties and their types
property_dict = {}

# Iterate over all the properties in the ontology
for s, p, o in g.triples((None, RDF.type, None)):
    if o in property_types:
        # If the property is of a type we are interested in, add it to the dictionary
        if s not in property_dict:
            property_dict[s] = []
        property_dict[s].append(str(o))

# Now we have a dictionary where the keys are properties and the values are lists of their types
# We can use this dictionary to validate the properties in the ontology

print("Properties and their types:")
for i in property_dict:
    print(i, property_dict[i])

for property, types in property_dict.items():
    if str(OWL.FunctionalProperty) in types:
        print(f"The property {property} is a Functional Property.")
        # Generate a prompt for the LLM to validate the property
        prompt = f"Given this ontology in a turtle file {g.serialize(format='turtle')}, validate if the property {property} is a Functional Property."
        response = model.generate_content(prompt)
        print(f"Validation result: {response.text}")

    elif str(OWL.SymmetricProperty) in types:
        print(f"The property {property} is a Symmetric Property.")
        # Generate a prompt for the LLM to validate the property
        prompt = f"Given this ontology in a turtle file {g.serialize(format='turtle')}, validate if the property {property} is a Symmetric Property."
        response = model.generate_content(prompt)
        print(f"Validation result: {response.text}")
    
    elif str(OWL.TransitiveProperty) in types:
        print(f"The property {property} is a Transitive Property.")
        # Generate a prompt for the LLM to validate the property
        prompt = f"Given this ontology in a turtle file {g.serialize(format='turtle')}, validate if the property {property} is a Transitive Property."
        response = model.generate_content(prompt)
        print(f"Validation result: {response.text}")
    
    elif str(OWL.ReflexiveProperty) in types:
        print(f"The property {property} is a Reflexive Property.")
        # Generate a prompt for the LLM to validate the property
        prompt = f"Given this ontology in a turtle file {g.serialize(format='turtle')}, validate if the property {property} is a Reflexive Property."
        response = model.generate_content(prompt)
        print(f"Validation result: {response.text}")
    
    else:
        print(f"The property {property} is not a Functional, Symmetric, Transitive, or Reflexive Property.")
        # Generate a prompt for the LLM to validate the property
        prompt = f"Given this ontology in a turtle file {g.serialize(format='turtle')}, validate if the property {property} is a Functional, Symmetric, Transitive, or Reflexive Property."
        response = model.generate_content(prompt)
        print(f"Validation result: {response.text}")