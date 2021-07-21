import json, random
from Item import Item
from Coins import Coins

# Inventory class which has a name, a list of items, a max weight and a list of coins
class Inventory:
    items = list()
    def __init__(self, name: str, max_weight = 150, items = [], coins = Coins.EMPTY, override = False):
        self.name = name
        self.override = override
        # TODO: Load
        self.max_weight = max_weight
        self.items = items
        self.coins = coins

    # add item to inventory
    # returns true if successful, false if not
    def addItem(self, item: Item):
        if self.getItemWeight() + self.getCoinWeight() + item.getWeight() * item.getAmount() <= self.max_weight:
            self.items.append(item)
            return True
        else:
            return False
    
    # remove an item from inventory
    # returns true if the item is there
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False

    # remove an amount of items from the inventory
    # returns true if all items could be removed, else false 
    # does not remove items if more are asked to be removed
    def removeAmount(self, item: Item, amount):
        for _item in self.items:
            if item.equals(_item):
                _item.remove(amount)
                return True
        return False

    # save the inventory to a json file
    def save(self):
        itemObjects = self.items.copy()
        self.items = []
        for item in itemObjects:
            self.items.append({
                'name': item.getName(),
                'amount': item.getAmount(),
                'weight': item.getWeight()
            })

        with open("inventories/" + self.name + '.json', 'w') as f:
            json.dump(self.__dict__, f, indent=4)

        self.items = itemObjects

    # calculate the total weight of the inventory
    def getItemWeight(self):
        weight = 0
        for item in self.items:
            weight += item.getWeight() * item.getAmount()
        return weight

    # add coins to inventory
    def addCoins(self, coins: Coins):
        if not coins.addCoins(self.coins):
            print("Failed to add coins " + coins + " to " + self.name + " (coins: " + str(self.coins) + ")")
            return False
        else:
            return True

# if name is main
if __name__ == '__main__':
    inventory = Inventory('test')

    inventory.save()
