import tkinter as tk
from tkinter import ttk, messagebox
import os
import json

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({}, file)
        self.load_contacts()

    def load_contacts(self):
        with open(self.filename, 'r') as file:
            self.contacts = json.load(file)

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            return False
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            self.save_contacts()
            return True

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            self.save_contacts()
            return True
        else:
            return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return True
        else:
            return False

    def search_contacts(self, keyword):
        return {name: details for name, details in self.contacts.items() if keyword.lower() in name.lower()}

class ContactBookGUI:
    def __init__(self, root):
        self.contact_book = ContactBook()

        self.root = root
        self.root.title("Contact Book")

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.name_var, width=40).grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.phone_var, width=40).grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.email_var, width=40).grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Add Contact", command=self.add_contact).grid(row=3, column=1, sticky=tk.W)
        ttk.Button(frame, text="Update Contact", command=self.update_contact).grid(row=4, column=1, sticky=tk.W)
        ttk.Button(frame, text="Delete Contact", command=self.delete_contact).grid(row=5, column=1, sticky=tk.W)

        ttk.Label(frame, text="Search:").grid(row=6, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.search_var, width=40).grid(row=6, column=1, sticky=(tk.W, tk.E))
        ttk.Button(frame, text="Search", command=self.search_contacts).grid(row=7, column=1, sticky=tk.W)

        self.contacts_listbox = tk.Listbox(frame, width=60, height=15)
        self.contacts_listbox.grid(row=8, column=0, columnspan=2, rowspan=5, sticky=(tk.W, tk.E))
        self.contacts_listbox.bind("<<ListboxSelect>>", self.on_select_contact)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()

        if name and phone and email:
            if self.contact_book.add_contact(name, phone, email):
                messagebox.showinfo("Success", "Contact added successfully")
                self.clear_fields()
                self.display_contacts()
            else:
                messagebox.showerror("Error", "Contact already exists")
        else:
            messagebox.showwarning("Input Error", "All fields are required")

    def update_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()

        if name and phone and email:
            if self.contact_book.update_contact(name, phone, email):
                messagebox.showinfo("Success", "Contact updated successfully")
                self.clear_fields()
                self.display_contacts()
            else:
                messagebox.showerror("Error", "Contact not found")
        else:
            messagebox.showwarning("Input Error", "All fields are required")

    def delete_contact(self):
        name = self.name_var.get().strip()

        if name:
            if self.contact_book.delete_contact(name):
                messagebox.showinfo("Success", "Contact deleted successfully")
                self.clear_fields()
                self.display_contacts()
            else:
                messagebox.showerror("Error", "Contact not found")
        else:
            messagebox.showwarning("Input Error", "Name is required")

    def search_contacts(self):
        keyword = self.search_var.get().strip()
        self.contacts_listbox.delete(0, tk.END)
        contacts = self.contact_book.search_contacts(keyword)
        for name, details in contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name} - {details['phone']} - {details['email']}")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        contacts = self.contact_book.contacts
        for name, details in contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name} - {details['phone']} - {details['email']}")

    def on_select_contact(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            contact = event.widget.get(index)
            name, phone, email = contact.split(' - ')
            self.name_var.set(name)
            self.phone_var.set(phone)
            self.email_var.set(email)

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.search_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    app.display_contacts()
    root.mainloop()
