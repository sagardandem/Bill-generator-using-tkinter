import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_total():
    try:
        discount = float(discount_entry.get()) if discount_entry.get() else 0
        selected_items = []
        for item, qty_entry in item_entries:
            quantity = int(qty_entry.get()) if qty_entry.get() else 0
            if quantity > 0:
                price = items[item]
                total_price = price * quantity
                discounted_price = total_price - (total_price * discount / 100)
                selected_items.append((item, quantity, discounted_price))

        for item, qty, price in selected_items:
            cart.append((item, qty, price))
            cart.append((item, qty, discounted_price))

        update_cart_display()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid quantity and discount values.")

def update_cart_display():
    cart_text = ""
    total_amount = 0
    for item, qty, price in cart:
        cart_text += f"{item} x{qty}: ₹{price:.2f}\n"
        total_amount += price

    cart_label.config(text=cart_text)
    total_label.config(text=f"Total Amount: ₹{total_amount:.2f}")

def proceed():
    if cart:
        messagebox.showinfo("Transaction Complete", "Transaction has been finalized.")
        reset()
    else:
        messagebox.showerror("Cart Empty", "Please add items to the cart before proceeding.")

def reset():
    for _, qty_entry in item_entries:
        qty_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    update_cart_display()

def update_datetime():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.config(text=now)
    root.after(1000, update_datetime)

root = tk.Tk()
root.title("SHOPY")
root.geometry("500x700")

items = {"Banana": 10, "Apple": 15, "Orange": 12, "Milk": 50, "Bread": 25}
cart = []
item_entries = []

title_frame = tk.Frame(root)
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="SHOPY", font=("Arial", 20, "bold"))
title_label.pack(side=tk.LEFT, padx=10)

datetime_label = tk.Label(title_frame, font=("Arial", 12))
datetime_label.pack(side=tk.RIGHT)
update_datetime()

item_frame = tk.Frame(root)
item_frame.pack(pady=10)

tk.Label(item_frame, text="Item", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(item_frame, text="Price (₹)", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
tk.Label(item_frame, text="Quantity", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)

for i, (item, price) in enumerate(items.items()):
    tk.Label(item_frame, text=item, font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)
    tk.Label(item_frame, text=f"₹{price}", font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)

    qty_var = tk.Entry(item_frame, width=5)
    qty_var.grid(row=i+1, column=2, padx=10, pady=5)

    item_entries.append((item, qty_var))

discount_frame = tk.Frame(root)
discount_frame.pack(pady=10)

tk.Label(discount_frame, text="Discount (%):", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
discount_entry = tk.Entry(discount_frame, width=10)
discount_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(root, text="Add to Cart", command=calculate_total, font=("Arial", 12))
add_button.pack(pady=10)

cart_frame = tk.Frame(root)
cart_frame.pack(pady=10)

tk.Label(cart_frame, text="Cart:", font=("Arial", 14, "bold")).pack()
cart_label = tk.Label(cart_frame, text="", font=("Arial", 12), justify=tk.LEFT)
cart_label.pack()

total_label = tk.Label(cart_frame, text="Total Amount: ₹0.00", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

proceed_button = tk.Button(button_frame, text="Proceed", command=proceed, font=("Arial", 14), bg="green", fg="white")
proceed_button.grid(row=0, column=0, padx=20)

cancel_button = tk.Button(button_frame, text="Cancel", command=reset, font=("Arial", 14), bg="red", fg="white")
cancel_button.grid(row=0, column=1, padx=20)

root.mainloop()
