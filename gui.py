## Funciones relacionadas con la interfaz gráfica:


import tkinter as tk
from tkinter import filedialog, messagebox
from main import main

def browse_file(entry_file_path):
    filename = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if filename:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filename)

def redact_file(entry_file_path):
    input_doc = entry_file_path.get()
    if not input_doc:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo .docx")
        return

    output_doc = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
    if not output_doc:
        return

    main(input_doc, output_doc)
    messagebox.showinfo("Información", "El archivo ha sido anonimizado y guardado correctamente.")

def create_gui():
    app = tk.Tk()
    app.title("Eliminación de Información Personal Identificable en Documentos Word V1")

    frame = tk.Frame(app, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label_file_path = tk.Label(frame, text="Seleccionar archivo .docx:")
    label_file_path.grid(row=0, column=0, sticky=tk.W)

    entry_file_path = tk.Entry(frame, width=50)
    entry_file_path.grid(row=1, column=0, pady=5)

    button_browse = tk.Button(frame, text="Buscar", command=lambda: browse_file(entry_file_path))
    button_browse.grid(row=1, column=1, padx=5)

    button_redact = tk.Button(frame, text="Anonimizar", command=lambda: redact_file(entry_file_path))
    button_redact.grid(row=2, column=0, columnspan=2, pady=10)

    app.mainloop()
