#! python3


def show_inventory(collection):
    print("Inventory:")
    for k in coll.keys():
        print(coll[k], k)
    print(f"Total number of items: {sum(v for v in coll.values())}")


# list to dictionary function for fantasy game inventory

def add_to_inventory(inventory, added_items):
    """
    Function to add new items to player inventory.
    :param inventory: players current inventory
    :param added_items: inventory of defeated dragon
    :return: updated inventory as dictionary
    """
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.update({item: 1})
    return inventory


coll = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

show_inventory(dragon_loot)
add_to_inventory(coll, dragon_loot)
print()
show_inventory(dragon_loot)
