def add_item(inventory, name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity


def remove_item(inventory, name, quantity):
    if name in inventory:
        inventory[name] -= quantity
        if inventory[name] < 0:
            inventory[name] = 0


def get_stock_report(inventory):
    report = ""
    for name in sorted(inventory):
        if inventory[name] > 0:
            report += name + ": " + str(inventory[name]) + "\n"
    return report.rstrip()

inv = {}

# add_item(inv, 'apples', 10)
# add_item(inv, 'bananas', 5)
# print(get_stock_report(inv))

add_item(inv, 'apples', 5)
remove_item(inv, 'bananas', 10)
print(get_stock_report(inv))

# remove_item(inv, 'oranges', 3)
# print(get_stock_report(inv))