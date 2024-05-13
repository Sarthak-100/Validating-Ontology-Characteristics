from utils.loader import load_ontology, load_model
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

from rdflib import Graph, Namespace

def preprocess_text(text):
    # Remove prefix, newline character, and asterisk
    processed_text = text.replace('http://www.iiitd.ac.in/sweb/inclass2#', '').strip().rstrip('*')
    return processed_text

def preprocess_text2(text):
    # Remove prefix, newline character, and asterisk
    processed_text = text.replace('http://www.w3.org/2002/07/owl#', '').strip().rstrip('*')
    processed_text = processed_text.replace('http://www.iiitd.ac.in/sweb/inclass2#', '').strip().rstrip('*')
    return processed_text

def extract_subproperties(ttl_file):
    # Create a RDF Graph
    g = Graph()
    
    # Bind the prefix 'rdfs' to its URL
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")  # Replace 'URL' with the actual URL
    
    # Parse the TTL file
    g.parse(ttl_file, format='turtle')
    
    # Dictionary to store subproperties
    subproperties = {}
    
    # Iterate over triples and extract subproperties
    for subj, pred, obj in g:
        if pred == rdfs.subPropertyOf:
            subj = str(subj)
            # obj = str(obj)
            subj = preprocess_text(subj)
            obj = preprocess_text2(obj)
            if subj in subproperties:
                subproperties[subj].append(obj)
            else:
                subproperties[subj] = [obj]
    
    return subproperties

# Example usage
ttl_file = 'C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/inclass_onto.ttl'
subproperties_dict = extract_subproperties(ttl_file)
print(subproperties_dict)

joblib.dump(subproperties_dict, "C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/subprop.joblib")