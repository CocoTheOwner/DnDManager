class Item:
    def __init__(self, name: str, weight: float, value: float, type: str, sellable = True):
        self.name = name
        self.weight = weight
        self.value = value
        self.type = type
        self.sellable = sellable

    def toJsonItem(self):
        info = {}
        for attr in dir(self):
            if not callable(getattr(self, attr)) and not attr.startswith("__"):
                info[attr] = getattr(self, attr)
        return info

    def fromJsonItem(data):
        try:
            return Item(data["name"], data["weight"], data["value"], data["type"], data["sellable"])
        except KeyError:
            print("Invalid datapoint. Recommend invalidating data in inventory.")
            return None