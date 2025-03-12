import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x500")
        self.root.configure(bg="#2C3E50")
        
        self.contacts = {}
        
        tk.Label(root, text="Contact Book", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)
        
        tk.Label(root, text="Name:", font=("Arial", 12), bg="#2C3E50", fg="white").pack()
        self.name_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=5)
        
        tk.Label(root, text="Phone:", font=("Arial", 12), bg="#2C3E50", fg="white").pack()
        self.phone_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.phone_entry.pack(pady=5)
        
        tk.Button(root, text="Add Contact", command=self.add_contact, font=("Arial", 12, "bold"), bg="#E74C3C", fg="white").pack(pady=5)
        tk.Button(root, text="View Contacts", command=self.view_contacts, font=("Arial", 12, "bold"), bg="#3498DB", fg="white").pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12, "bold"), bg="#1ABC9C", fg="white").pack(pady=5)
        
        self.listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, bg="#ECF0F1")
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        
        if name and phone:
            self.contacts[name] = phone
            self.listbox.insert(tk.END, f"{name}: {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number")
    
    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.listbox.insert(tk.END, f"{name}: {phone}")
    
    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            contact_text = self.listbox.get(selected[0])
            name = contact_text.split(": ")[0]
            del self.contacts[name]
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

root = tk.Tk()
app = ContactBook(root)
root.mainloop()
