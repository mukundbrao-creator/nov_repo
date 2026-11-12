import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        root.title("Restaurant Management App")
        root.geometry("800x600")
        self.menu = {"FRIES MEAL": 2, "LUNCH MEAL": 2, "BURGER MEAL": 3, "PIZZA MEAL": 4, "CHEESE BURGER": 2.5, "DRINKS": 1}
        self.rate = 82
        self.background()

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=2, pady=10)

        self.labels, self.entries = {}, {}

        for i, (item, price) in enumerate(self.menu.items(), 1):
            label = ttk.Label(frame, text=f"{item} (${price}):")
            label.grid(row=i, column=0, padx=10, pady=5)
            self.labels[item] = label

            entry = ttk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[item] = entry

        self.currency = tk.StringVar(value="USD")
        ttk.Label(frame, text="Currency:").grid(row=7, column=0)

        ttk.Combobox(frame, textvariable=self.currency, values=("USD", "INR"), state = "readonly").grid(row=7, column=1)
        self.currency.trace("w", self.update_prices)

        ttk.Button(frame, text="Place Order", command=self.place_order).grid(row=8, columnspan=2, pady=10)

    def background(self):
        canvas = tk.Canvas(self.root, width=800, height=600)
        canvas.pack()
        image = tk.PhotoImage(file="background.png")
        image = image.subsample(max(1, image.width() // 800), max(1, image.height() // 600))

        canvas.create_image(0, 0, anchor = tk.NW, image=image)
        canvas.image = image
    def update_prices(self, *args):
        rate = self.rate if self.currency.get() == "INR" else 1
        symbol = "₹" if self.currency.get() == "INR" else "$"

        for item, label in self.labels.items():
            label.config(text=f"{item} ({symbol}{self.manu[item] * rate}):")
    def place_order(self):
        rate = self.rate if self.currency.get() == "INR" else 1
        symbol = "₹" if self.currency.get() == "INR" else 1
        total, summary = 0, "Order Summary:\n"

        for item, entry in self.entries.items():
            quantity = entry.get()
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                price = self.menu[item] * rate
                cost = quantity * price
                total += cost
                summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if total:
            messagebox.showinfo("Order Placed", summary +f"\nTotal Cost: {symbol}{total}")
        else:
                messagebox.showerror("Error", "Please order at least one item.")
root = tk.Tk()
app=RestaurantOrderManagement(root)
root.mainloop()