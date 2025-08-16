import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Path to your JSON file
JSON_FILE = "tools.json"

# Load existing data or create empty list if file doesn't exist
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as f:
        tools_data = json.load(f)
else:
    tools_data = []

# Categories mapping
CATEGORIES = [
    "home", "doc", "convert", "design", "study", "price",
    "math", "write", "code", "travel", "business", "mail", "lock"
]

# Function to add new tool
def add_tool():
    name = name_entry.get().strip()
    link = link_entry.get().strip()
    description = desc_entry.get().strip()
    category = category_var.get()
    featured = featured_var.get()

    if not name or not link or not description:
        messagebox.showerror("Error", "Name, Link, and Description are required!")
        return

    new_tool = {
        "name": name,
        "link": link,
        "description": description,
        "logo": f"logos/{name.replace(' ', '').lower()}.png",
        "category": category,
        "featured": featured
    }

    tools_data.append(new_tool)

    # Save updated JSON
    with open(JSON_FILE, "w") as f:
        json.dump(tools_data, f, indent=4)

    messagebox.showinfo("Success", f"Tool '{name}' added successfully!")

    # Clear the form
    name_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    category_var.set(CATEGORIES[0])
    featured_var.set(False)

# --- GUI Setup ---
root = tk.Tk()
root.title("Add Online Tool")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Link:").grid(row=1, column=0, sticky="e")
link_entry = tk.Entry(root, width=50)
link_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, sticky="e")
desc_entry = tk.Entry(root, width=50)
desc_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Category:").grid(row=3, column=0, sticky="e")
category_var = tk.StringVar(value=CATEGORIES[0])
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=CATEGORIES, state="readonly")
category_dropdown.grid(row=3, column=1, padx=5, pady=5)

featured_var = tk.BooleanVar()
featured_check = tk.Checkbutton(root, text="Featured", variable=featured_var)
featured_check.grid(row=4, column=1, sticky="w", padx=5, pady=5)

add_button = tk.Button(root, text="Add Tool", command=add_tool)
add_button.grid(row=5, column=1, pady=10)

root.mainloop()
