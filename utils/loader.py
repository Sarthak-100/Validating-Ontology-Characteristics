from rdflib import Graph
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDGKwoz1Aqf750-cKGmerJG3L7c-YO3bIg"

def load_ontology(ontology_url):
    # Create a new graph
    g = Graph()

    # Parse the ontology from the given URL
    g.parse(ontology_url, format='turtle')

    return g

def load_model():
    genai.configure(api_key=GOOGLE_API_KEY)
    print("Available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    print("\nUsing model: gemini-pro")

    model = genai.GenerativeModel('gemini-pro')

    return model

    