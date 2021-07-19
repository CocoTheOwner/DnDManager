from Inventory import Inventory
from Commander import Commander
from Items import Item
print([i for i in dir(Inventory) if (not i.startswith("__")) and callable(getattr(Inventory, i))])
i = Inventory("Lazarus")
i.addItem(Item("sword", 5, 7, "weapon", True), 5)
i.save()
c = Commander(
    "v0.0.1", 
    [i],
    {},
    run=False
)
c.run()