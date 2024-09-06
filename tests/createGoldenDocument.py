import json
from document_processing import load_document
from pii_detection import identify_pii


def extract_entities_from_doc(input_file, output_json):
    # Cargar el documento
    doc = load_document(input_file)
    if not doc:
        print("No se pudo cargar el documento.")
        return

    entities_list = []

    for para in doc.paragraphs:
        text = para.text
        if text.strip():  # Ignorar párrafos vacíos
            entities = identify_pii(text)
            entities_list.append({
                "text": text,
                "entities": [{"start": start, "end": end, "label": label} for start, end, label in entities]
            })

    # Guardar el resultado en un archivo JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(entities_list, f, ensure_ascii=False, indent=4)

    print(f"Entidades extraídas y guardadas en {output_json}")


# Ejecutar la extracción
input_file = "Sworn4.docx"
output_json = "GoldenSworn4.json"
extract_entities_from_doc(input_file, output_json)
