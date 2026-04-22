file_path = "db.txt"

# Function to calc the amount of prizes able to redeemed
def redeem_prizes(points):
    prizes = 0
    threshold = 5
    while points >= threshold:
        prizes += 1
        threshold *= 2
    return prizes

#load the scores from the file
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

#create file if none found then write current scores to file
def save_scores(sales):
    with open(file_path, "w") as f:
        for name, points in sales.items():
            f.write(f"{name},{points}\n")

def start():
    sales, order = load_scores()
    print("COOKIE DOUGH SALES POINTS AND PRIZES TRACKER")
    print("")
    print("--------------------------------------------")
    print("")
    print(f"Current Points Per User")

    # Prints All Current Scores
    for name_nospace in order:
        points = sales[name_nospace]
        print(
            f"{name_nospace} has {points} points and can redeem {redeem_prizes(points)} prize(s)."
        )
    print("")

def addtoscores():


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

def print_scores():
    print("Selling over! Let's see how everyone did!")
    for name_nospace in order:
        points = sales[name_nospace]
        print(
            f"{name_nospace} has {points} points and can redeem {redeem_prizes(points)} prize(s)."
        )


start()
addtoscores()
print_scores()
# add_or_remove = 0
# while True:
#     add_or_remove = input("Would you like to add to the scores or redeem your prizes? ")

#     if add_or_remove.lower != "yes" or "no":
#         print("Please only enter Yes/No")
#     else:
#         break
    
# print("working")
