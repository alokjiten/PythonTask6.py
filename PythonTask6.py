import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

# Sample product data
products = {
    "Product1": 100,
    "Product2": 200,
    "Product3": 300,
    "Product4": 400,
    "Product5": 500
}

# Function to add product to the bill
def add_product():
    product = product_combobox.get()
    quantity = quantity_entry.get()
    if product and quantity.isdigit():
        price = products[product]
        total_price = price * int(quantity)
        bill_text.insert(tk.END, f"{product}\t{quantity}\t{price}\t{total_price}\n")
        update_total(total_price)
    else:
        messagebox.showerror("Input Error", "Please select a product and enter a valid quantity.")

# Function to update total amount
def update_total(amount):
    current_total = float(total_label['text'])
    new_total = current_total + amount
    total_label.config(text=f"{new_total:.2f}")

# Function to generate invoice
def generate_invoice():
    customer_name = customer_name_entry.get()
    customer_phone = customer_phone_entry.get()
    if customer_name and customer_phone:
        invoice_window = tk.Toplevel(window)
        invoice_window.title("Invoice")
        invoice_text = tk.Text(invoice_window, width=50, height=20)
        invoice_text.pack()
        invoice_text.insert(tk.END, f"Customer Name: {customer_name}\n")
        invoice_text.insert(tk.END, f"Customer Phone: {customer_phone}\n")
        invoice_text.insert(tk.END, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        invoice_text.insert(tk.END, "----------------------------------------\n")
        invoice_text.insert(tk.END, bill_text.get("1.0", tk.END))
        invoice_text.insert(tk.END, f"Total: {total_label['text']}\n")
        invoice_text.insert(tk.END, "----------------------------------------\n")
        invoice_text.insert(tk.END, "Thank you for your purchase!")
    else:
        messagebox.showerror("Input Error", "Please enter customer details.")

# Main window
window = tk.Tk()
window.title("Billing Software")
window.geometry("600x400")

# Customer details
customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_label.pack(pady=5)
customer_name_entry = tk.Entry(window)
customer_name_entry.pack(pady=5)

customer_phone_label = tk.Label(window, text="Customer Phone:")
customer_phone_label.pack(pady=5)
customer_phone_entry = tk.Entry(window)
customer_phone_entry.pack(pady=5)

# Product selection
product_label = tk.Label(window, text="Select Product:")
product_label.pack(pady=5)
product_combobox = ttk.Combobox(window, values=list(products.keys()))
product_combobox.pack(pady=5)

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack(pady=5)
quantity_entry = tk.Entry(window)
quantity_entry.pack(pady=5)

add_button = tk.Button(window, text="Add to Bill", command=add_product)
add_button.pack(pady=10)

# Bill area
bill_text = tk.Text(window, width=50, height=10)
bill_text.pack(pady=10)

# Total amount
total_label = tk.Label(window, text="0.00")
total_label.pack(pady=5)

# Generate invoice button
generate_invoice_button = tk.Button(window, text="Generate Invoice", command=generate_invoice)
generate_invoice_button.pack(pady=10)

window.mainloop()
