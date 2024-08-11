#  Graphical user interface

import tkinter as tk
from tkinter import filedialog, messagebox
from main import main

# Global variable to track whether the enhanced visual mode is active
modo_mejorado = False

# Function to toggle the enhanced visual mode on or off
def toggle_modo_mejorado(frame, entry_file_path, label_file_path, button_browse, button_redact):
    global modo_mejorado
    modo_mejorado = not modo_mejorado
    apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact)

# Function to apply styles based on the visual mode (normal or enhanced)
def apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact):
    if not modo_mejorado:
        # Normal mode styles
        frame.config(bg="SystemButtonFace")
        label_file_path.config(bg="SystemButtonFace", fg="black", font=("Arial", 10))
        entry_file_path.config(bg="white", fg="black", font=("Arial", 10))
        button_browse.config(bg="SystemButtonFace", fg="black", font=("Arial", 10))
        button_redact.config(bg="SystemButtonFace", fg="black", font=("Arial", 10))
    else:
        # Enhanced visual mode styles
        frame.config(bg="black")
        label_file_path.config(bg="black", fg="white", font=("Arial", 14, "bold"))
        entry_file_path.config(bg="black", fg="yellow", font=("Arial", 14, "bold"))
        button_browse.config(bg="gray", fg="white", font=("Arial", 14, "bold"))
        button_redact.config(bg="gray", fg="white", font=("Arial", 14, "bold"))

# Function to open a file dialog to browse for a .docx file and insert its path into the entry widget
def browse_file(entry_file_path):
    filename = filedialog.askopenfilename(filetypes=[("Documentos Word", "*.docx")])
    if filename:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filename)

# Function to handle the file redaction process
def redact_file(entry_file_path):
    # Get the input document path from the entry widget
    input_doc = entry_file_path.get()
    if not input_doc:
        # Show a warning if no file was selected
        messagebox.showwarning("Atención", "Por favor seleccione un fichero .docx")
        return

    # Open a file dialog to save the redacted file
    output_doc = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Documento Word", "*.docx")])
    if not output_doc:
        # If the operation is cancelled, do nothing
        return

    # Call the main function to process the file
    main(input_doc, output_doc)
    # Show a confirmation message once the file has been redacted and saved
    messagebox.showinfo("Informacion", "El fichero ha sido anonimizado y guardado correctamente.")

# Function to display an "About" dialog with information about the application
def show_about_dialog():
    messagebox.showinfo("About", "Anonimyzer v1.0\n\nAplicacion para eliminar infomracion personal identificable en documentos Word.")

# Function to display a "Help" dialog with usage instructions
def show_help_dialog():
    messagebox.showinfo("Help", "1. Seleccione un fichero .docx.\n2. Click 'Anonimizar' para eliminar informacion personal.\n3. Use 'Modo mejora Visual' si requiere mejora visual.")

# Function to create the main GUI window
def create_gui():
    # Create the main application window
    app = tk.Tk()
    app.title("Anonimizador de información personal")

    # Menu bar
    menu_bar = tk.Menu(app)
    app.config(menu=menu_bar)

    # Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Help", command=show_help_dialog)
    help_menu.add_separator()
    help_menu.add_command(label="About", command=show_about_dialog)

    # Main frame
    frame = tk.Frame(app, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    # Label for file path
    label_file_path = tk.Label(frame, text="Seleccione un fichero .docx :")
    label_file_path.grid(row=0, column=0, sticky=tk.W)

    # Entry widget to display the selected file path
    entry_file_path = tk.Entry(frame, width=50)
    entry_file_path.grid(row=1, column=0, pady=5)

    # Button to browse for a file
    button_browse = tk.Button(frame, text="Buscar", command=lambda: browse_file(entry_file_path))
    button_browse.grid(row=1, column=1, padx=5)

    # Button to redact the selected file
    button_redact = tk.Button(frame, text="Anonimizar", command=lambda: redact_file(entry_file_path))
    button_redact.grid(row=2, column=0, columnspan=2, pady=10)

    # Button to toggle the enhanced visual mode
    button_modo = tk.Button(frame, text="Modo Mejora Visual",
                            command=lambda: toggle_modo_mejorado(frame, entry_file_path, label_file_path, button_browse, button_redact))
    button_modo.grid(row=3, column=0, columnspan=2, pady=10)

    # Apply the initial style (normal mode)
    apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact)

    # Start the main event loop of the application
    app.mainloop()

# Call the function to create the GUI and start the application
create_gui()
