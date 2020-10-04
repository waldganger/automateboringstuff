inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inv(inv):
    total = 0
    for k, v in inv.items():
        total += v
        print(f"{v} {k}")
    print(f"Total number of items: {total}")

display_inv(inv)

# List to Dictionary Function for Fantasy Game Inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory

print(add_to_inventory(inv, dragonLoot))
print(add_to_inventory(inv, dragonLoot))