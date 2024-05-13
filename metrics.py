def compute_metrics(Ref_len, Pred_len, Inter_len):
    # Calculate the intersection of Mpred and Mref for true positives
    true_positives = Inter_len

    # Precision: |Mpred ∩ Mref| / |Mpred|
    precision = true_positives / Pred_len

    # Recall: |Mpred ∩ Mref| / |Mref|
    recall = true_positives / Ref_len

    # F1 Score: 2 * (Precision * Recall) / (Precision + Recall)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score

