import json

from document_processing import load_document
from pii_detection import identify_pii


def calculate_metrics(true_entities, detected_entities):
    """
    Calculate precision, recall, and F1-score based on the comparison between
    the true entities and the detected entities.

    Args:
        true_entities (list): A list of tuples representing the true entities
                              in the format (start, end, label).
        detected_entities (list): A list of tuples representing the entities
                                  detected by the application in the format (start, end, label).

    Returns:
        tuple: A tuple containing precision, recall, and F1-score.
    """
    # Convert lists of entities to sets for comparison
    true_set = set((ent['start'], ent['end'], ent['label']) for ent in true_entities)
    detected_set = set((start, end, label) for start, end, label in detected_entities)

    tp = len(true_set & detected_set)  # Intersection between true_set and detected_set (True Positives)
    fp = len(detected_set - true_set)  # Elements in detected_set but not in true_set (False Positives)
    fn = len(true_set - detected_set)  # Elements in true_set but not in detected_set (False Negatives)

    # Calculate precision, recall, and F1-score
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1

# Load the Golden Document
with open("GoldenSworn4.json", "r", encoding="utf-8") as f:
    true_data = json.load(f)

# Extract the true entities
true_entities = []
for item in true_data:
    true_entities.extend(item["entities"])

# Load the document and extract the text
doc = load_document("Sworn1.docx")
detected_entities = []
for para in doc.paragraphs:
    text = para.text
    if text.strip():  # Ignore empty paragraphs
        entities = identify_pii(text)
        detected_entities.extend(entities)

# Calculate metrics
precision, recall, f1 = calculate_metrics(true_entities, detected_entities)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
