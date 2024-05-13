from utils.loader import load_ontology, load_model
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from metrics import compute_metrics

def modify_word_set(word_set):
    """
    Modify a set of words by removing redundant "/n-" characters from the end of each word.
    
    Args:
    - word_set (set): The input set of words.
    
    Returns:
    - set: The modified set of words with words without redundant "/n-" characters.
    """
    modified_word_set = set()
    for word in word_set:
        # Remove "/n-" from the end of each word if present
        modified_word = word.rstrip("\n-")
        modified_word_set.add(modified_word)
    return modified_word_set

# Example usage


def modify_dict_keys(dictionary):
    """
    Modify dictionary keys by removing redundant "/n-" characters from the end.
    
    Args:
    - dictionary (dict): The input dictionary.
    
    Returns:
    - dict: The modified dictionary with keys without redundant "/n-" characters.
    """
    modified_dict = {}
    for key, value in dictionary.items():
        # Remove "/n-" from the end of each key if present
        modified_key = key.rstrip("\n-")
        modified_dict[modified_key] = value
    return modified_dict

# Example usage



lpred = joblib.load("C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/similar_prop.joblib")

lorg = joblib.load("C:/Users/Aaditya Gupta/OneDrive/Desktop/sweb_final_project/Validating-Ontology-Characteristics/subprop.joblib")

input_dict = lpred
lpred = modify_dict_keys(input_dict)
print(lpred)
print(lorg)

print("---------------------------------------------")

key_pred = set(lpred.keys())
key_org = set(lorg.keys())
key_ints = key_org.intersection(key_pred)

# print(key_pred,key_org)
# print(key_ints)

for k in key_ints:
    print(k)
    # input_word_set = {'word/n-', 'another_word/n-', 'last_word/n-'}
    # modified_word_set = modify_word_set(input_word_set)
    # print(modified_word_set)
    s2 = modify_word_set(set(lpred[k]))
    s1 = modify_word_set(set(lorg[k]))
    print(s1,s2)
    result = len(s1.intersection(s2)) +1
    print("Precision, Recall and F1 score are:",compute_metrics(len(s1),len(s2), result))
    
