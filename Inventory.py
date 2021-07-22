import json, random
from Item import Item
from Coin import Coin

# Inventory class which has a name, a list of items, a max weight and a list of coins
class Inventory:
    name: str
    items = None
    coins = None
    max_weight = None

    def __init__(self, name: str, items = [], coins = Coin.EMPTY.copy(), max_weight = 150, override = False):
        self.name = name
        self.load(items, coins, max_weight)

    # add item to inventory
    # returns true if successful, false if not
    def addItem(self, item: Item):
        if self.getInventoryWeight() + Coin.getCoinWeight(self.coins) + item.getWeight() * item.getAmount() <= self.max_weight:
            self.items.append(item)
            return True
        else:
            return False

    # add coins to inventory
    def addCoin(self, coin: Coin):
        if not coin.addTo(self.coins):
            print("Failed to add coin " + coin + " to " + self.name + " (coins: " + str(self.coins) + ")")
            return False
        else:
            return True
    
    # remove an item from inventory regardless of the amount
    # returns true if the item is there
    def removeItem(self, item: Item, amount = -1):
        if item in self.items:
            if amount == -1:
                self.items.remove(item)
                return True
            else:
                for _item in self.items:
                    if item.equals(_item):
                        _item.remove(amount)
                        return True
        return False
        
    # calculate the total weight of the inventory
    def getInventoryWeight(self):
        weight = 0
        for item in self.items:
            weight += item.getWeight() * item.getAmount()
        return weight

    # get inventory weight left
    def getInventoryLeft(self):
        return self.max_weight - self.getInventoryWeight()

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

    # load the inventory from a json file
    def load(self, altItems: list, altCoins: dict, altMaxWeight: int):
        with open("inventories/" + self.name + '.json', 'r') as f:
            data = json.load(f)
            self.__dict__.update(data)
            self.items = []
            for item in data['items']:
                self.items.append(Item(item['name'], item['amount'], item['weight']))

            # check if items, coins and max weight are set
            if self.items is None or self.coins is None or self.max_weight is None:
                if self.items == None:
                    self.items = altItems
                if self.coins == None:
                    self.coins = altCoins
                if self.max_weight == None:
                    self.max_weight = altMaxWeight
                return False
            return True

    # reset the inventory using the emptyInventory.json file
    def reset(self):
        with open("emptyInventory.json", 'r') as f:
            data = json.load(f)
            name = self.name
            self.__dict__.update(data)
            self.name = name
            self.save()

# if name is main
if __name__ == '__main__':
    inventory = Inventory('test')
    inventory.reset()
