import tkinter as tk
from tkinter import ttk

class NotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad App")
        self.geometry("600x700")
        self.resizable(True, True)
        
        # Titlebar
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        setting_menu = tk.Menu(menubar, tearoff=0)
        setting_menu.add_command(label="Settings", command=self.settings)
        menubar.add_cascade(label="Settings", menu=setting_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", command=self.help)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

        # Ribbon
        ribbon = ttk.Frame(self, height=25)
        ribbon.pack(side="top", fill="x")
        
        bold_button = ttk.Button(ribbon, text="Bold")
        bold_button.pack(side="left", padx=5)

        italic_button = ttk.Button(ribbon, text="Italic")
        italic_button.pack(side="left", padx=5)

        underline_button = ttk.Button(ribbon, text="Underline")
        underline_button.pack(side="left", padx=5)

        # Text area
        self.text = tk.Text(self)
        self.text.pack(expand=True, fill="both")

    def new_file(self):
        # Code to create a new file
        pass

    def open_file(self):
        # Code to open a file
        pass

    def save_file(self):
        # Code to save the current file
        pass

    def save_file_as(self):
        # Code to save the current file with a different name
        pass

    def settings(self):
        # Code to show the settings dialog
        pass

    def help(self):
        # Code to show the help dialog
        pass

if __name__ == "__main__":
    app = NotepadApp()
    app.mainloop()
