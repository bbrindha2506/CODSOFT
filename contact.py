import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        root.configure(bg="#D90166")
        
        
        self.contacts = {}
        
        
        self.create_widgets()
    
    def create_widgets(self):
        
        title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 20),bg="#D90166")
        title_label.pack(pady=10)
        
        
        detail_frame = tk.Frame(self.root,bg="#D90166")
        detail_frame.pack(pady=10)


        tk.Label(detail_frame, text="Name:",bg="#D90166").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(detail_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(detail_frame, text="Phone:",bg="#D90166").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(detail_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        
        
        button_frame = tk.Frame(self.root,bg="#D90166")
        button_frame.pack(pady=10)

        
        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact,bg="#b2eebe")
        add_button.grid(row=0, column=0, padx=5)
        
        edit_button = tk.Button(button_frame, text="Edit Contact", command=self.edit_contact,bg="#ffa1bd")
        edit_button.grid(row=0, column=1, padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact,bg="#b01717")
        delete_button.grid(row=0, column=2, padx=5)
        
        
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_select_contact)
    
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            messagebox.showwarning("Input Error", "Both name and phone are required!")
            return
        if name in self.contacts:
            messagebox.showwarning("Duplicate Contact", "Contact already exists!")
            return
        self.contacts[name] = phone
        self.update_contact_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")

    def edit_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        name = self.contact_listbox.get(selected[0])
        phone = self.phone_entry.get().strip()
        if not phone:
            messagebox.showwarning("Input Error", "Phone is required to update the contact!")
            return
        self.contacts[name] = phone
        self.update_contact_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")
    
    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        name = self.contact_listbox.get(selected[0])
        del self.contacts[name]
        self.update_contact_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def on_select_contact(self, event):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected[0])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, self.contacts[name])
    
    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, name)
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


root = tk.Tk()
app = ContactBook(root)
root.mainloop()
