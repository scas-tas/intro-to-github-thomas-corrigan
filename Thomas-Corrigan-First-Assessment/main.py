import random

# Enable colours on Windows (safe on all systems)
try:
    from colorama import init
    init()
except:
    pass

# Colours
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"


# File selection
while True:
    file_path = input("Please enter file name/directory (blank = scores.txt): ")
    if file_path != "":
        break
    else:
        print(YELLOW + "Default directory selected: scores.txt" + RESET)
        file_path = "scores.txt"
        break


sales = {}
order = []

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


def line():
    print(CYAN + "=" * 55 + RESET)


def small_line():
    print(BLUE + "-" * 55 + RESET)


def redeem_prizes(points):
    prizes = 0
    threshold = 5
    while points >= threshold:
        prizes += 1
        threshold *= 2
    return prizes


def get_random_prize():
    return random.choice(prizes)


def load_scores():
    try:
        with open(file_path, "r") as f:
            for line_text in f:
                line_text = line_text.strip()
                if line_text == "":
                    continue
                name, points = line_text.split(",")
                sales[name] = int(points)
                order.append(name)
    except FileNotFoundError:
        pass

    return sales, order


def save_scores(sales):
    with open(file_path, "w") as f:
        for name, points in sales.items():
            f.write(f"{name},{points}\n")


def show_scores(title):
    print()
    line()
    print(BOLD + title.center(55) + RESET)
    line()

    if len(order) == 0:
        print(YELLOW + "No scores saved yet." + RESET)
    else:
        for name in order:
            points = sales[name]
            available = redeem_prizes(points)

            print(BOLD + name + RESET)
            print(f"  {GREEN}Points:{RESET} {points}")
            print(f"  {MAGENTA}Redeemable:{RESET} {available}")
            small_line()
    print()


def start():
    load_scores()

    print()
    line()
    print(BOLD + "COOKIE DOUGH SALES TRACKER".center(55) + RESET)
    line()

    show_scores("CURRENT SCORES")

    while True:
        choice = input("Do you want to redeem prizes? (yes/no): ").lower().strip()

        if choice == "yes":
            redeem()
            break
        elif choice == "no":
            addtoscores()
            break
        else:
            print(RED + "Please enter yes or no." + RESET)


def addtoscores():
    print()
    line()
    print(BOLD + "ADD SCORES".center(55) + RESET)
    line()

    while True:
        name = input("Name (blank to finish): ").title().strip()

        if name == "":
            break

        while True:
            amount_input = input("Cookie dough sold: ")
            try:
                amount = int(amount_input)
                break
            except ValueError:
                print(RED + "Please enter a valid whole number." + RESET)

        if name in sales:
            sales[name] += amount
        else:
            sales[name] = amount
            order.append(name)

        print(GREEN + f"✔ Added {amount} points to {name}" + RESET)
        print(CYAN + f"{name} now has {sales[name]} points" + RESET)
        small_line()

        save_scores(sales)

    # 👇 THIS is what you wanted (runs AFTER adding scores)
    while True:
        choice = input("Do you want to redeem prizes now? (yes/no): ").lower().strip()

        if choice == "yes":
            redeem()
            break
        elif choice == "no":
            break
        else:
            print(RED + "Please enter yes or no." + RESET)


def print_scores():
    show_scores("FINAL SCORES")


def redeem():
    print()
    line()
    print(BOLD + "REDEEM PRIZE".center(55) + RESET)
    line()

    name = input("Name to redeem: ").title().strip()

    if name not in sales:
        print(RED + "That person does not exist." + RESET)
        return

    points = sales[name]
    prizes_available = redeem_prizes(points)

    if prizes_available == 0:
        print(RED + f"{name} does not have enough points to redeem." + RESET)
        return

    print()
    print(f"{name} has {GREEN}{points}{RESET} points")
    print(f"Can redeem: {MAGENTA}{prizes_available}{RESET} prize(s)")
    print()

    confirm = input("Redeem ONE prize? (yes/no): ").lower().strip()

    if confirm == "yes":
        cost = 5
        while points >= cost * 2:
            cost *= 2

        reward = get_random_prize()
        sales[name] -= cost

        print()
        line()
        print(BOLD + YELLOW + "PRIZE REDEEMED".center(55) + RESET)
        line()
        print(f"{BOLD}Student:{RESET} {name}")
        print(f"{GREEN}Cost:{RESET} {cost} points")
        print(f"{MAGENTA}Prize won:{RESET} {reward}")
        print(f"{CYAN}Remaining:{RESET} {sales[name]} points")
        line()

        save_scores(sales)
    else:
        print(YELLOW + "Redeem cancelled." + RESET)


start()
print_scores()