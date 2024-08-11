## Funciones de identificacion de las NER
import re
import spacy
from utils import remove_accents

# Load model
nlp = spacy.load("en_core_web_md")

def identify_pii(text):
    normalized_text = remove_accents(text)
    doc = nlp(normalized_text)
    pii_entities = []

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "ORG", "DATE", "TIME", "ORDINAL", "CARDINAL", "LOC"]:
            pii_entities.append((ent.start_char, ent.end_char, ent.label_))

    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    for match in email_regex.finditer(text):
        pii_entities.append((match.start(), match.end(), "EMAIL"))

    id_regex = re.compile(r'\bnumber:\s*([a-zA-Z0-9]+)\b', re.IGNORECASE)
    for match in id_regex.finditer(text):
        start, end = match.span(1)
        pii_entities.append((start, end, "ID"))

    return pii_entities

