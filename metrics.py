def compute_metrics(Mpred, Mref):
    # Calculate the intersection of Mpred and Mref for true positives
    true_positives = len(Mpred.intersection(Mref))

    # Precision: |Mpred ∩ Mref| / |Mpred|
    precision = true_positives / len(Mpred)

    # Recall: |Mpred ∩ Mref| / |Mref|
    recall = true_positives / len(Mref)

    # F1 Score: 2 * (Precision * Recall) / (Precision + Recall)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score

