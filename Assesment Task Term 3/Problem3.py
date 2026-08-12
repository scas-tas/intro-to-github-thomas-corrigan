def add_item(inventory, name, quantity):
    if name in inventory:   # Check if the item already exists in the dictionary and add to the existing value. 
        inventory[name] += quantity
    else:                   # if not then add it
        inventory[name] = quantity


def remove_item(inventory, name, quantity):
    if name in inventory:  # Check if the item exists in the dictionary so it dosent error out
        inventory[name] -= quantity
        if inventory[name] < 0:
            inventory[name] = 0


def get_stock_report(inventory):
    report = ""
    for name in sorted(inventory):
        if inventory[name] > 0:         
             report += name + ": " +  str(inventory[name]) +"\n"  # Make report by addthing name of item and the amount as a string
    return report.strip()


# If I was to add the get_total_items(inventory) function i would do it like this

def get_total_items(inventory):
    counter = 0
    for amount in inventory.values():
        counter += amount
    return counter

inv = {} # Make the dictionary

# add_item(inv, 'apples', 10)
# add_item(inv, 'bananas', 5)
# print(get_stock_report(inv))

add_item(inv, 'apples', 5)
remove_item(inv, 'bananas', 10)
print(get_stock_report(inv))

# remove_item(inv, 'oranges', 3)
# print(get_stock_report(inv))

print(get_total_items(inv))
