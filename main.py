##  Punto de entrada a nuestro programa:

from document_processing import load_document, save_document
from redaction import redact_document
from pii_detection import identify_pii

def main(input_file, output_file):
    doc = load_document(input_file)
    if doc:
        redacted_doc = redact_document(doc, identify_pii)
        save_document(redacted_doc, output_file)

if __name__ == "__main__":
    from gui import create_gui
    create_gui()
