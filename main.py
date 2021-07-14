from Inventory import Inventory
from Commander import Commander
print([i for i in dir(Inventory) if (not i.startswith("__")) and callable(getattr(Inventory, i))])
i = Inventory("Lazarus")
print(i.save.desc)
c = Commander(
    "v0.0.1", 
    [i],
    {},
    run=False
)
c.run()