
# *GUI OK
# *Problemas: Aglutina en una pagina
#     No respeta el tamaño de la tipografia.
#   Falla con muchas entidades
#       El modelo es ENG SM y falla con muchas PERSON in Catalan.
#               Usado CAt y peor)
#           Para testear otros modelos: python -m spacy download en_core_web_md y pip uninstall en-core-web-md
#               Los salva en:.venv\Lib\site-packages\en_core_web_sm

#   Remplaza con "REDACTED --c cambiar a "Eliminado" o la Entidad.



import docx
import spacy
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Load model
nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("ca_core_news_sm")
#nlp = spacy.load("en_core_web_trf")


# Load and Read Word Document
def load_document(file_path):
    return docx.Document(file_path)

# Identify PII using NER and REGEX
def identify_pii(text):
    doc = nlp(text)
    pii_entities = []
    # Use SpaCy for standard PII detection
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "ORG", "ORDINAL", "CARDINAL", "LOC"]:
            pii_entities.append((ent.start_char, ent.end_char, ent.label_))
    # Custom regex for email addresses
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    for match in email_regex.finditer(text):
        pii_entities.append((match.start(), match.end(), "EMAIL"))

    # Custom regex for passport numbers (generic example)
    passport_regex = re.compile(r'[A-PR-WY][1-9]\d\s?\d{4}[1-9]')
    for match in passport_regex.finditer(text):
        pii_entities.append((match.start(), match.end(), "PASSPORT"))

    print(pii_entities)
    return pii_entities


#  Redact PII
def redact_text(text, pii_entities):
    redacted_text = text
    offset = 0
    for start, end, label in pii_entities:
        redacted_text = redacted_text[:start + offset] + "[REDACTED]" + redacted_text[end + offset:]
        offset += len("[REDACTED]") - (end - start)
    return redacted_text


#  Process Text and Replace entities
def redact_document(doc):
    for para in doc.paragraphs:
        text = para.text
        pii_entities = identify_pii(text)
        redacted_text = redact_text(text, pii_entities)
        para.text = redacted_text
    return doc


#  Save Redacted Document
def save_document(doc, output_path):
    doc.save(output_path)


# Main function to tie everything
def main(input_file, output_file):
    doc = load_document(input_file)
    redacted_doc = redact_document(doc)
    save_document(redacted_doc, output_file)


#  Gui:
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if filename:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filename)


def redact_file():
    input_doc = entry_file_path.get()
    if not input_doc:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo .docx")
        return

    output_doc = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
    if not output_doc:
        return

    main(input_doc, output_doc)
    messagebox.showinfo("Información", "El archivo ha sido anonimizado y guardado correctamente.")


app = tk.Tk()
app.title("Eliminación de Información Personal Identificable en Documentos Word V1")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_file_path = tk.Label(frame, text="Seleccionar archivo .docx:")
label_file_path.grid(row=0, column=0, sticky=tk.W)

entry_file_path = tk.Entry(frame, width=50)
entry_file_path.grid(row=1, column=0, pady=5)

button_browse = tk.Button(frame, text="Buscar", command=browse_file)
button_browse.grid(row=1, column=1, padx=5)

button_redact = tk.Button(frame, text="Anonimizar", command=redact_file)
button_redact.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()