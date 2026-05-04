import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

FILE_PATH = "scores.txt"

sales = {}
prizes = [
    "Mars Bar",
    "KitKat",
    "Skittles packet",
    "Zooper Dooper",
    "Packet of chips (Smiths)",
    "Chocolate milk",
    "Free canteen sausage roll",
    "Free $10 canteen voucher"
]


# ---------------- LOGIC ---------------- #

def redeem_prizes(points):
    count = 0
    threshold = 5
    while points >= threshold:
        count += 1
        threshold *= 2
    return count


def calculate_total_cost(points, amount):
    cost = 5
    total = 0
    temp = points

    for _ in range(amount):
        while temp >= cost * 2:
            cost *= 2
        total += cost
        temp -= cost

    return total


def load_scores():
    if not os.path.exists(FILE_PATH):
        return

    with open(FILE_PATH, "r") as f:
        for line in f:
            if line.strip():
                name, pts = line.strip().split(",")
                sales[name] = int(pts)


def save_scores():
    with open(FILE_PATH, "w") as f:
        for name, pts in sales.items():
            f.write(f"{name},{pts}\n")


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Cookie Dough Tracker")
root.geometry("650x500")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="#2b2b2b",
                foreground="white",
                fieldbackground="#2b2b2b",
                rowheight=28)

style.configure("Treeview.Heading",
                background="#444",
                foreground="white",
                font=("Segoe UI", 10, "bold"))

style.map("Treeview", background=[("selected", "#0078d7")])


# ---------------- TABLE ---------------- #

tree = ttk.Treeview(root, columns=("Points", "Redeemable"), show="headings")
tree.heading("Points", text="Points")
tree.heading("Redeemable", text="Redeemable")

tree.column("Points", width=100, anchor="center")
tree.column("Redeemable", width=120, anchor="center")

tree.pack(fill="both", expand=True, padx=10, pady=10)


def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for name, pts in sales.items():
        tree.insert("", "end", iid=name, values=(pts, redeem_prizes(pts)))

    update_dropdown()


# ---------------- ADD SECTION ---------------- #

add_frame = tk.Frame(root, bg="#1e1e1e")
add_frame.pack(pady=5)

tk.Label(add_frame, text="Name", fg="white", bg="#1e1e1e").grid(row=0, column=0)
tk.Label(add_frame, text="Amount", fg="white", bg="#1e1e1e").grid(row=0, column=1)

name_entry = tk.Entry(add_frame)
name_entry.grid(row=1, column=0, padx=5)

amount_entry = tk.Entry(add_frame)
amount_entry.grid(row=1, column=1, padx=5)


def add_score():
    name = name_entry.get().title().strip()
    try:
        amount = int(amount_entry.get())
    except:
        messagebox.showerror("Error", "Enter a number")
        return

    if not name:
        return

    sales[name] = sales.get(name, 0) + amount

    save_scores()
    refresh_table()

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


tk.Button(add_frame, text="Add Score", command=add_score, bg="#0078d7", fg="white").grid(row=1, column=2, padx=10)


# ---------------- REDEEM SECTION ---------------- #

redeem_frame = tk.Frame(root, bg="#1e1e1e")
redeem_frame.pack(pady=10)

tk.Label(redeem_frame, text="Select Student", fg="white", bg="#1e1e1e").grid(row=0, column=0)

selected_name = tk.StringVar()
dropdown = ttk.Combobox(redeem_frame, textvariable=selected_name, state="readonly")
dropdown.grid(row=1, column=0, padx=5)

tk.Label(redeem_frame, text="Amount", fg="white", bg="#1e1e1e").grid(row=0, column=1)

redeem_entry = tk.Entry(redeem_frame, width=5)
redeem_entry.grid(row=1, column=1)


def update_dropdown():
    dropdown["values"] = list(sales.keys())


def redeem(amount=None):
    name = selected_name.get()

    if name not in sales:
        return

    points = sales[name]
    max_p = redeem_prizes(points)

    if max_p == 0:
        messagebox.showinfo("Info", "Not enough points")
        return

    if amount is None:
        try:
            amount = int(redeem_entry.get())
        except:
            messagebox.showerror("Error", "Enter a number")
            return

    if amount <= 0 or amount > max_p:
        messagebox.showerror("Error", f"Max is {max_p}")
        return

    total_cost = calculate_total_cost(points, amount)

    rewards = [random.choice(prizes) for _ in range(amount)]
    sales[name] -= total_cost

    save_scores()
    refresh_table()

    result = "\n".join(f"• {r}" for r in rewards)

    messagebox.showinfo(
        "Redeemed",
        f"{name} redeemed {amount} prize(s)\n\n"
        f"Cost: {total_cost}\n"
        f"Remaining: {sales[name]}\n\n"
        f"{result}"
    )


tk.Button(redeem_frame, text="Redeem", command=lambda: redeem(), bg="#28a745", fg="white").grid(row=1, column=2, padx=5)

tk.Button(redeem_frame, text="Redeem Max", command=lambda: redeem(redeem_prizes(sales.get(selected_name.get(), 0))),
          bg="#ff9800", fg="black").grid(row=1, column=3, padx=5)


# ---------------- START ---------------- #

load_scores()
refresh_table()

root.mainloop()