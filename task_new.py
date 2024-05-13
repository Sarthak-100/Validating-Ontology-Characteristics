from utils.loader import load_ontology, load_model
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib


def preprocess_text(text):
    # Remove prefix, newline character, and asterisk
    processed_text = text.replace('http://dbpedia.org/ontology/', '').strip().rstrip('*')
    return processed_text

model_2 = SentenceTransformer('all-mpnet-base-v2')

g = load_ontology("C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/inclass_ontology.ttl")
model = load_model()
print(g)
intro = "Our project aims to develop a system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs)"
query = "Create a list of all the properties and sub-properties present in the ontology."

q = intro +"Given this ontology in a turtle file " +  g.serialize(format="turtle") +  "Perform this task and give appropriate solution: " + query
response1 = model.generate_content(q)
text = response1.text


print(response1.text)


processed_text = preprocess_text(text)
l = processed_text.split(" ")
emd = []
for i in range(len(l)):
    emd.append(model_2.encode(l[i]))
joblib.dump(l,"C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/list.joblib" )

emd = np.array(emd)
print(emd.shape)

cos = np.zeros(len(emd)*len(emd)).reshape(len(emd), len(emd))
for i in range(len(emd)):
    for j in range(len(emd)):
        a = emd[i].reshape(1,-1)
        b = emd[j].reshape(1,-1)
        cos[i][j] = cosine_similarity(a,b)

index=[]
for i in range(len(cos)):
    top_indices = np.argsort(cos[i])[-5:]
    index.append(top_indices)

joblib.dump(index,"C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/index.joblib" )
joblib.dump(cos,"C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/cosine.joblib" )

similar_prop={}
for i in range(len(index)):
    p=l[i]
    similar_prop[p] = []
    for j in index[i]:
        similar_prop[p].append(l[j])
print(similar_prop)
joblib.dump(similar_prop,"C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/similar_prop.joblib" )




# Example usage:
# text = 'http://dbpedia.org/ontology/silverMedalist/n*'
# processed_text = preprocess_text(text)
# print(processed_text)
