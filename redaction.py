##  Funciones para anonimizar el texto:
from document_processing import has_page_break


def redact_text(text, pii_entities):
    redacted_text = text
    offset = 0
    for start, end, label in pii_entities:
        replacement_text = f"[{label}]"
        redacted_text = redacted_text[:start + offset] + replacement_text + redacted_text[end + offset:]
        offset += len(replacement_text) - (end - start)
    return redacted_text

def redact_document(doc, identify_pii):
    for para in doc.paragraphs:
        if has_page_break(para):
            continue
        text = para.text
        pii_entities = identify_pii(text)
        redacted_text = redact_text(text, pii_entities)
        para.text = redacted_text
    return doc
