file_path = "db.txt"


def redeem_prizes(points):
    prizes = 0
    threshold = 5
    while points >= threshold:
        prizes += 1
        threshold *= 2
    return prizes

file_path = "db.txt"


def load_scores():
    sales = {}
    order = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                name, points = line.strip().split(",")
                sales[name] = int(points)
                order.append(name)
    except FileNotFoundError:
        pass  # file doesn't exist yet

    return sales, order


def save_scores(sales):
    with open(file_path, "w") as f:
        for name, points in sales.items():
            f.write(f"{name},{points}\n")


print("COOKIE DOUGH SALES POINTS AND PRIZES TRACKER")

# sales = {}
# order = []
sales, order = load_scores()
# Changed to using the file

# Create Blank List And Dictionary

while True:

    name = input("Name: ").title()
    if name == "":  # See if Name is blank and exit the loop if it is
        break

    name_nospace = name.strip()

    while True: 
        amount_input = input("Cookie dough sold: ") 
        try: 
            amount = int(amount_input) 
            break 
        except ValueError:
            print("Please enter a valid integer for the cookie dough sold.")
    # breakpoint()
    if name in sales:
        sales[name_nospace] += amount
    else:
        sales[name_nospace] = amount
        order.append(name_nospace)
    save_scores(sales)

print("Selling over! Let's see how everyone did!")

for name_nospace in order:
    points = sales[name_nospace]
    print(
        f"{name_nospace} has {points} points and can redeem {redeem_prizes(points)} prize(s)."
    )
