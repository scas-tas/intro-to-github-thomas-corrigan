def redeem_prizes(points):
    prizes = 0
    threshold = 5
    while points >= threshold:
        prizes += 1
        threshold *= 2
    return prizes


print("COOKIE DOUGH SALES POINTS AND PRIZES TRACKER")

sales = {}
order = []

# Create Blank List And Dictionary

while True:
    name = input("Name: ")
    if name == "":  # See if Name is blank and exit the loop if it is
        break

    name_lower = name.lower()
    name_nospace = name.strip()

    # Remove The Spaces And Start and End of string
    # Without this I get error
    # "Traceback (most recent call last): File "c:\Users\tacor\Documents\GitHub\intro-to-github-thomas-corrigan\Thomas-Corrigan-First-Assessment\main.py",
    # line 38, in <module>points = sales[name.strip()]~~~~~
    # ^^^^^^^^^^^^^^
    # KeyError: ''"

    # Assuming this error is complaining about the space but this solution seems to work

    while True:
        amount_input = input("Cookie dough sold: ")
        amount = int(amount_input)
        break
    # breakpoint()
    if name in sales:
        sales[name_nospace] += amount
    else:
        sales[name_nospace] = amount
        order.append(name_nospace)

print("Selling over! Let's see how everyone did!")

for name_nospace in order:
    points = sales[name_nospace]
    print(
        f"{name_nospace} has {points} points and can redeem {redeem_prizes(points)} prize(s)."
    )

