import json, os, traceback
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
        if self.getInventoryWeight() + self.getCoinWeight() + item.getWeight() * item.getAmount() <= self.max_weight:
            if item in self.items:
                item.add(item.amount)
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
        weight += self.getCoinWeight()
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
        # check that file exists
        if not os.path.isfile("inventories/" + self.name + '.json'):
            print("Inventory " + self.name + " does not exist, creating default")
            # copy inventories/default.json to the inventories folder with the name of the inventory
            with open("inventories/default.json", 'r') as f:
                with open("inventories/" + self.name + '.json', 'w') as f2:
                    f2.write(f.read())

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

    # reset the inventory using the inventories/default.json file
    def reset(self):
        with open("inventories/default.json", 'r') as f:
            data = json.load(f)
            name = self.name
            self.__dict__.update(data)
            self.name = name
            self.save()

    # remove the inventory from the inventory folder
    def remove(self):
        os.remove("inventories/" + self.name + '.json')

    
    # condense coins to copper
    # 1 platinum is 500 copper
    # 1 gold is 100 copper
    # 1 electrum is 50 copper
    # 1 silver is 10 copper
    # condenses everything to gold coins, silver coins and copper coins
    # returns none if the coins dictionary is invalid 
    # (does not contain all PLATINUM, GOLD, ELECTRUM, SILVER, COPPER)
    def condenseCoins(coins: dict, toPlat: False):
        
        if not Coin.isValid(coins):
            return None

        copper = coins[Coin.COPPER] \
        + coins[Coin.SILVER]   * 10 \
        + coins[Coin.ELECTRUM] * 50 \
        + coins[Coin.GOLD]     * 100\
        + coins[Coin.PLATINUM] * 500\

        print(copper)

        if toPlat:
            coins[Coin.PLATINUM] = copper // 500
            copper = copper % 500
        else:
            coins[Coin.PLATINUM] = 0
        
        coins[Coin.GOLD]     = copper // 100
        copper = copper % 100
        coins[Coin.SILVER]   = copper // 10
        copper = copper % 10
        coins[Coin.COPPER]   = copper

        coins[Coin.ELECTRUM] = 0
        return coins
        
    # calculate the total weight of the coins
    # returns -1 if invalid coins dict
    def getCoinWeight(self):
        if not Coin.isValid(self.coins):
            return -1

        weight = 0
        for coinType in self.coins:
            weight += self.coins[coinType] * Coin.weight
        return weight

# if name is main
if __name__ == '__main__':
    # run tests on a copy of the default inventory
    try:
        inventory = Inventory('test')
        inventory.reset()
        item = Item('Potion', 1, 10)
        item.addToOverrideDatabase(True, "misc", 0.5)        
        inventory.addItem(item)
        inventory.addCoin(Coin('gold', 5))
        coinWeight = inventory.getCoinWeight()
        inventory.save()
        weight = inventory.getInventoryWeight()
        weightLeft = inventory.getInventoryLeft()
        item.removeFromDatabase()
        inventory.remove()
    except Exception as e:
        # print a traceback
        print("Exception raised during inventory test: " + e)
        traceback.print_exc()
