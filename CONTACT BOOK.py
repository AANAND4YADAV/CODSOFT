import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Manager")
        self.geometry("500x400")
        self.resizable(0, 0)

        self.contacts = self.load_contacts()

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Add Contact", command=self.add_contact, font=("Arial", 12)).pack(pady=10)
        tk.Button(self, text="View Contacts", command=self.view_contacts, font=("Arial", 12)).pack(pady=10)
        tk.Button(self, text="Search Contact", command=self.search_contact, font=("Arial", 12)).pack(pady=10)
        tk.Button(self, text="Quit", command=self.quit, font=("Arial", 12)).pack(pady=10)

        self.contacts_listbox = tk.Listbox(self, font=("Arial", 12))
        self.contacts_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.contacts_listbox.bind('<Double-1>', self.on_double_click)

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        contact_info = self.get_contact_info()
        if contact_info:
            self.contacts.append(contact_info)
            self.save_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.view_contacts()

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            results = [c for c in self.contacts if search_query.lower() in c['name'].lower() or search_query in c['phone']]
            self.contacts_listbox.delete(0, tk.END)
            for contact in results:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def on_double_click(self, event):
        selection = self.contacts_listbox.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            self.edit_contact(contact, index)

    def edit_contact(self, contact, index):
        new_info = self.get_contact_info(contact)
        if new_info:
            self.contacts[index] = new_info
            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.view_contacts()

    def get_contact_info(self, contact=None):
        name = simpledialog.askstring("Contact Info", "Enter name:", initialvalue=contact['name'] if contact else "")
        if not name:
            return None
        phone = simpledialog.askstring("Contact Info", "Enter phone number:", initialvalue=contact['phone'] if contact else "")
        if not phone:
            return None
        email = simpledialog.askstring("Contact Info", "Enter email:", initialvalue=contact['email'] if contact else "")
        address = simpledialog.askstring("Contact Info", "Enter address:", initialvalue=contact['address'] if contact else "")
        return {"name": name, "phone": phone, "email": email, "address": address}

    def quit(self):
        self.destroy()

if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
