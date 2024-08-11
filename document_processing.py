## Cargar, guardar, y manipular documentos.

import docx
from tkinter import messagebox

def load_document(file_path):
    try:
        return docx.Document(file_path)
    except docx.opc.exceptions.PackageNotFoundError:
        messagebox.showerror("Error", "El archivo está en uso. Por favor, ciérrelo antes de procesarlo.")
        return None

def save_document(doc, output_path):
    doc.save(output_path)

def has_page_break(para):
    return para._element.xpath('.//w:br[@w:type="page"]')

def add_page_break(para):
    run = para.add_run()
    run.add_break(docx.text.run.WD_BREAK.PAGE)
