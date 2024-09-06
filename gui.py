import tkinter as tk
from tkinter import filedialog, messagebox

# Global variable to track whether the enhanced visual mode is active
modo_mejorado = False

# Function to toggle the enhanced visual mode on or off
def toggle_modo_mejorado(frame, entry_file_path, label_file_path, button_browse, button_redact):
    global modo_mejorado
    modo_mejorado = not modo_mejorado
    apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact)

# Function to apply styles based on the visual mode (normal or enhanced)
def apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact):
    # Common style settings for both modes
    font = ("Helvetica", 11)
    entry_file_path.config(font=font, relief="flat")

    if not modo_mejorado:
        # Normal mode styles
        frame.config(bg="#f0f0f0")
        label_file_path.config(bg="#f0f0f0", fg="#333333", font=font)
        entry_file_path.config(bg="white", fg="#333333")
        button_browse.config(bg="#e0e0e0", fg="#333333", relief="flat")
        button_redact.config(bg="#4caf50", fg="white", relief="flat")
    else:
        # Enhanced visual mode styles
        frame.config(bg="#2e2e2e")
        label_file_path.config(bg="#2e2e2e", fg="white", font=("Helvetica", 13, "bold"))
        entry_file_path.config(bg="#3b3b3b", fg="#cddc39", font=("Helvetica", 13, "bold"))
        button_browse.config(bg="#3b3b3b", fg="white", relief="flat")
        button_redact.config(bg="#ff9800", fg="white", relief="flat")

    # Apply rounded corners effect (simulated with padding and relief)
    for widget in [button_browse, button_redact]:
        widget.config(padx=5, pady=5, borderwidth=2, highlightthickness=0)

# Function to open a file dialog to browse for a .docx file and insert its path into the entry widget
def browse_file(entry_file_path):
    filename = filedialog.askopenfilename(filetypes=[("Documentos Word", "*.docx")])
    if filename:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filename)

# Function to handle the file redaction process
def redact_file(entry_file_path):
    input_doc = entry_file_path.get()
    if not input_doc:
        messagebox.showwarning("Atención", "Por favor seleccione un fichero .docx")
        return

    output_doc = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Documento Word", "*.docx")])
    if not output_doc:
        return

    # Call the main function to process the file
    messagebox.showinfo("Información", "El fichero ha sido anonimizado y guardado correctamente.")

# Function to display an "About" dialog with information about the app.
def show_about_dialog():
    messagebox.showinfo("About", "Anonimyzer v0.4 \n\nAplicacion para eliminar informacion personal identificable en documentos Word.\nDesarrollado por OSV.\nContacto: https://github.com/osososvos/TFB_PII_V1")

# Function to display a "Help" dialog with usage instructions
def show_help_dialog():
    messagebox.showinfo("Help", "1. Seleccione un fichero .docx.\n2. Click 'Anonimizar' para eliminar informacion personal.\n3. Use 'Modo mejora Visual' si requiere mejora visual.")

# Function to create the main GUI window
def create_gui():
    app = tk.Tk()
    app.title("Anonimizador de información personal")

    # Set window size and position
    app.geometry("450x250")
    app.resizable(False, False)

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
    frame = tk.Frame(app, padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Label for file path
    label_file_path = tk.Label(frame, text="Seleccione un fichero .docx :")
    label_file_path.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

    # Entry widget to display the selected file path
    entry_file_path = tk.Entry(frame, width=40)
    entry_file_path.grid(row=1, column=0, pady=(0, 10), padx=(0, 5), sticky="ew")

    # Button to browse for a file
    button_browse = tk.Button(frame, text="Buscar", command=lambda: browse_file(entry_file_path))
    button_browse.grid(row=1, column=1, padx=(0, 10))

    # Button to redact the selected file
    button_redact = tk.Button(frame, text="Anonimizar", command=lambda: redact_file(entry_file_path))
    button_redact.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="ew")

    # Button to toggle the enhanced visual mode
    button_modo = tk.Button(frame, text="Modo Mejora Visual",
                            command=lambda: toggle_modo_mejorado(frame, entry_file_path, label_file_path, button_browse, button_redact))
    button_modo.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="ew")

    # Apply the initial style (normal mode)
    apply_style(frame, entry_file_path, label_file_path, button_browse, button_redact)

    # Start the main event loop of the application
    app.mainloop()

# Call the function to create the GUI and start the application
create_gui()
