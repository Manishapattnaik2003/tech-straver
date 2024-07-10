import tkinter as tk
from tkinter import ttk, messagebox
import os

class NotesApp:
    def __init__(self, filename="notes.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass

    def add_note(self, note):
        with open(self.filename, 'a') as file:
            file.write(note + "\n")

    def get_notes(self):
        with open(self.filename, 'r') as file:
            return file.readlines()

    def update_notes(self, notes):
        with open(self.filename, 'w') as file:
            file.writelines(notes)

class NotesAppGUI:
    def __init__(self, root):
        self.notes_app = NotesApp()

        self.root = root
        self.root.title("Notes App")

        self.note_text = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame, text="Note:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.note_text, width=40).grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Add Note", command=self.add_note).grid(row=0, column=2, sticky=tk.W)
        ttk.Button(frame, text="Display Notes", command=self.display_notes).grid(row=1, column=2, sticky=tk.W)
        ttk.Button(frame, text="Update Note", command=self.update_note).grid(row=2, column=2, sticky=tk.W)
        ttk.Button(frame, text="Delete Note", command=self.delete_note).grid(row=3, column=2, sticky=tk.W)
        ttk.Button(frame, text="Search Notes", command=self.search_notes).grid(row=4, column=2, sticky=tk.W)

        self.notes_listbox = tk.Listbox(frame, width=60, height=15)
        self.notes_listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky=(tk.W, tk.E))
        self.notes_listbox.bind("<<ListboxSelect>>", self.on_select_note)

    def add_note(self):
        note = self.note_text.get()
        if note:
            self.notes_app.add_note(note)
            self.note_text.set("")
            self.display_notes()
        else:
            messagebox.showwarning("Input Error", "Note cannot be empty")

    def display_notes(self):
        self.notes_listbox.delete(0, tk.END)
        notes = self.notes_app.get_notes()
        for note in notes:
            self.notes_listbox.insert(tk.END, note.strip())

    def on_select_note(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            note = event.widget.get(index)
            self.note_text.set(note)

    def update_note(self):
        selection = self.notes_listbox.curselection()
        if selection:
            index = selection[0]
            notes = self.notes_app.get_notes()
            notes[index] = self.note_text.get() + "\n"
            self.notes_app.update_notes(notes)
            self.display_notes()
            self.note_text.set("")
        else:
            messagebox.showwarning("Selection Error", "Please select a note to update")

    def delete_note(self):
        selection = self.notes_listbox.curselection()
        if selection:
            index = selection[0]
            notes = self.notes_app.get_notes()
            del notes[index]
            self.notes_app.update_notes(notes)
            self.display_notes()
            self.note_text.set("")
        else:
            messagebox.showwarning("Selection Error", "Please select a note to delete")

    def search_notes(self):
        keyword = self.note_text.get()
        self.notes_listbox.delete(0, tk.END)
        notes = self.notes_app.get_notes()
        found_notes = [note.strip() for note in notes if keyword.lower() in note.lower()]
        for note in found_notes:
            self.notes_listbox.insert(tk.END, note)
        if not found_notes:
            messagebox.showinfo("Search Result", "No notes found with that keyword")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesAppGUI(root)
    root.mainloop()
