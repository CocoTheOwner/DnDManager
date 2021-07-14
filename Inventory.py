from Items import Item
from Storage import Storage
from functools import wraps

ITEM = "item"
AMOUNT = "amount"

def Command(desc):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            func.desc = desc
            print(func.desc)
            print(desc)
            return func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


class Inventory:

    def __init__(self, name: str, items = {str: [Item, int]}):
        self.name = name
        self.items = items

    def __init__(self, name: str):
        self.name = name
        self.load()

    def __call__(self):
        print("==========================================")
        print("{} Inventory List:".format(self.name))
        print(" * ({}) Total - W: {} / V: {}".format(len(self.items), -1, -1))
        for item in self.items:
            print(" - ({}) {} - W: {} / V: {} / S: {}".format(
                self.items[item][AMOUNT], 
                item, 
                self.items[item][ITEM].weight,
                self.items[item][ITEM].value,
                self.items[item][ITEM].type,
                self.items[item][ITEM].sellable
            ))
        print("==========================================")

    @Command("Save the selected inventory to file")
    def save(self):
        Storage.save({"name": self.name, "items": self.toJsonItems()}, "items/" + self.name + ".json")

    def toJsonItems(self):
        items = {}
        for item in self.items:
            items[item] = {"properties": self.items[item][ITEM].toJsonItem(), "amount": self.items[item][AMOUNT]}
        return items

    @Command("Reload the selected inventory from file")
    def load(self):
        data = Storage.load("items/" + self.name + ".json", {"name": self.name, "items": {}})
        self.items = Inventory.fromJsonItems(data["items"])

    def fromJsonItems(items):
        itemList = {}
        for item in items:
            props = Item.fromJsonItem(items[item]["properties"])
            if props is None:
                print("Invalid item returned to inventory. Skipping datapoint. Recommend invalidating.")
                continue
            itemList[item] = {ITEM: props, AMOUNT: items[item][AMOUNT]}
        if len(itemList) == 0:
            print("Empty inventory. If there are invalid items, please invalidate and reset.")
        return itemList

    @Command("Removes a number of items by name and amount")
    def removeItems(self, nameOrItem, amount: int):
        if type(nameOrItem) is str:
            if not nameOrItem in self.items:
                print("Item {} not in {}'s inventory!".format(nameOrItem, self.name))
                return
            self.items[nameOrItem][AMOUNT] = max(self.items[nameOrItem][AMOUNT] - amount, 0)
        else:
            self.removeItems(nameOrItem.name, amount)
    
    @Command("Deletes an item from the inventory, regardless of the amount")
    def deleteItem(self, nameOrItem):
        if type(nameOrItem) is str:
            if not nameOrItem in self.items:
                print("Item {} not in {}'s inventory! Could not delete!".format(nameOrItem, self.name))
                return
            del(self.items[nameOrItem])
        else:
            self.deleteItem(nameOrItem.name)

    @Command("Adds a number of items to the inventory by name")
    def addItem(self, nameOrItem: str, amount: int):
        if type(nameOrItem) is str:
            if not nameOrItem in self.items:
                print("Item {} not in {}'s inventory! Not enough info to add new item!".format(nameOrItem, self.name))
                return
            self.items[nameOrItem][AMOUNT] += amount
        else:
            if not nameOrItem in self.items:
                print("Item {} not in {}'s inventory! Adding new item!".format(nameOrItem.name, self.name))
                self.items[nameOrItem.name] = {ITEM: nameOrItem, AMOUNT: amount}
                return
            self.items[nameOrItem.name][AMOUNT] += amount

    @Command("Sets any item to have any amount in the inventory")
    def setItem(self, nameOrItem, amount: int):
        if type(nameOrItem) is str:
            if not nameOrItem in self.items:
                print("Item {} not in {}'s inventory!".format(nameOrItem, self.name))
                return
            self.items[nameOrItem][AMOUNT] = max(amount, 0)
        else:
            self.setItem(nameOrItem.name, amount)

    @Command("Retrieve the amount of items of a specific item")
    def getItemAmount(self, name):
        if type(name) is str:
            return self.items[name][AMOUNT]
        return self.items[name.name][AMOUNT]

    @Command("Get the item object by a specific name")
    def getItemItem(self, name: str):
        return self.items[name][ITEM]
