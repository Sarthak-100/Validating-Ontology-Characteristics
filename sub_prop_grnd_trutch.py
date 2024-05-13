from utils.loader import load_ontology, load_model
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

g = load_ontology("class_ttls_prop/SportsTeam.ttl")



