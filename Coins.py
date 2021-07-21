class Coins:

    def __init__(self, type: str, amount: int):
        self.type = type
        self.amount = amount

    PLATINUM = "platinum"
    GOLD = "gold"
    ELECTRUM = "electrum"
    SILVER = "silver"
    COPPER = "copper"

    EMPTY = {COPPER: 0, SILVER: 0, GOLD: 0, ELECTRUM: 0, PLATINUM: 0}

    weight = 0.02

    # condense coins to copper
    # 1 platinum is 500 copper
    # 1 gold is 100 copper
    # 1 electrum is 50 copper
    # 1 silver is 10 copper
    # condenses everything to gold coins, silver coins and copper coins
    # returns none if the coins dictionary is invalid 
    # (does not contain all PLATINUM, GOLD, ELECTRUM, SILVER, COPPER)
    def condenseCoins(coins: dict, toPlat: False):
        
        if not Coins.isValid(coins):
            return None

        copper = coins[Coins.COPPER] \
        + coins[Coins.SILVER]   * 10 \
        + coins[Coins.ELECTRUM] * 50 \
        + coins[Coins.GOLD]     * 100\
        + coins[Coins.PLATINUM] * 500\

        print(copper)

        if toPlat:
            coins[Coins.PLATINUM] = copper // 500
            copper = copper % 500
        else:
            coins[Coins.PLATINUM] = 0
        
        coins[Coins.GOLD]     = copper // 100
        copper = copper % 100
        coins[Coins.SILVER]   = copper // 10
        copper = copper % 10
        coins[Coins.COPPER]   = copper

        coins[Coins.ELECTRUM] = 0
        return coins
        
    # calculate the total weight of the coins
    # returns -1 if invalid coins dict
    def getCoinWeight(coins: dict):
        if not Coins.isValid(coins):
            return -1

        weight = 0
        for coinType in coins:
            weight += coins[coinType] * Coins.weight
        return weight

    # check if a coin dictionary is valid
    def isValid(coins: dict):
        for coinType in Coins.EMPTY:
            if not coinType in coins:
                return False
        return True

    # add coins to a coins dictionary
    # returns false is the coins dict is not valid
    def addCoins(self, coins: dict):
        if not Coins.isValid(coins):
            return False

        coins[self.type] += self.amount
        return True
