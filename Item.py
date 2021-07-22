import json

# Item class, has a name, this amount thisd a price
class Item:

    name: str
    amount: int
    price: float

    sellable = None
    type = None
    weight = None


    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.loadProperties()

    # Add this item to the amount
    def add(self, amount: int):
        self.amount += amount

    # Remove this item from the amount
    def remove(self, amount: int):
        self.amount -= amount

    # Get the amount of this item
    def getAmount(self):
        return self.amount
    
    # Set the amount of this item
    def setAmount(self, amount: int):
        self.amount = amount

    # Get the price of this item
    def getPrice(self):
        return self.price

    # Set the price of this item
    def setPrice(self, price: float):
        self.price = price

    # Get the name of this item
    def getName(self):
        return self.name

    # Get if this item is sellable
    def getSellable(self):
        return self.sellable

    # Get the type of this item
    def getType(self):
        return self.type

    # Get the weight of this item
    def getWeight(self):
        return self.weight

    # Compare this item to another item based on name and amount
    def equals(self, item: 'Item'):
        return self.name == item.getName() and self.amount == item.getAmount()

    # Get the properties of this item from the ItemDatabase.json file
    def loadProperties(self):
        with open('ItemDatabase.json') as f:
            data = json.load(f)
        if self.name in data:
            self.sellable = data[self.name]['sellable']
            self.type = data[self.name]['type']
            self.weight = data[self.name]['weight']
        else:
            print("Item " + self.name + " not in database! Set item properties with Item#addToDatabase")
            self.sellable = None
            self.type = None
            self.weight = None

    # Set the properties of this item to the ItemDatabase.json file
    def saveProperties(self):
        with open('ItemDatabase.json', 'r+') as f:
            data = json.load(f)
            data[self.name] = {
                'sellable': self.sellable,
                'type': self.type,
                'weight': self.weight
            }
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    # Add this item to the ItemDatabase json
    def addToOverrideDatabase(self, sellable: bool, type: str, weight: float):
        self.sellable = sellable
        self.type = type
        self.weight = weight
        self.saveProperties()
        return self.isValid()
            
    # Validate the item to make sure it has properties
    def isValid(self):
        return self.sellable is not None and self.type is not None and self.weight is not None

    # Remove and item from the ItemDatabase.json file
    # Returns true if removed, false if not in there
    def removeFromDatabase(name: str):
        with open('ItemDatabase.json', 'r+') as f:
            data = json.load(f)
            if name in data:
                del data[name]
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                return True
            else:
                return False

# if name is main print the json serialized item
if __name__ == '__main__':
    item = Item('dummy', 1, 1)
    print(item.isValid())
    if not item.isValid():
        item.addToDatabase(True, 'dummy', 1)
    print(item.isValid())
