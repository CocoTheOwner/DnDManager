import time

class Commander():

    file = "commander.txt"

    loadedInventory = None

    lines = [["============ INFO SECTION ============"],
            ["============ HELP SECTION ============"],
            ["=========== TABLE SECTION ============"],
            ["========== COMMAND SECTION ==========="]]

    def __init__(self, version: str, inventories: list, commands: dict, done = False, run = True):

        self.version = version # vX.X.X
        self.inventories = inventories # [Inventory, Inventory, ...]
        self.commands = commands # {"command_name": {"function": Function, "description": "description"}, ...}
        self.done = done # True/False

        self.addLine(self.Lines.INFO, "D&D Inventory Commander - " + self.version)
        self.addLine(self.Lines.INFO, "Loaded Inventories: " + ", ".join([inv.name for inv in inventories]))
        self.addLine(self.Lines.INFO, "Selected Inventory: " + self.loadedInventory)

        self.writeLines()

        self.tick()

        if run: self.run()

    def run(self):
        tick = 0
        while not self.done:
            tick += 1
            self.tick()
            if tick % 6000 == 0:
                print("Ticked 60 seconds (6000 iterations)")
            time.sleep(0.01)

    def tick(self):
        1 + 1

    def commandHandle(self, line: str):
        if line.__contains__("exit"):
            self.done = True
        

    def stop(self):
        self.done = True

    class Lines:
        INFO = 0
        HELP = 1
        TABLE = 2
        COMMAND = 3

    def addLine(self, type: Lines, line: str):
        self.lines[type].append(line)

    def writeLines(self):
        string = ""
        for section in self.lines:
            string += "\n".join(section) + "\n\n"
        open(self.file, "w+").write(string)