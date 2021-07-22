class Coin:

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
    def condenseCoin(coins: dict, toPlat: False):
        
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
    def getCoinWeight(coins: dict):
        if not Coin.isValid(coins):
            return -1

        weight = 0
        for coinType in coins:
            weight += coins[coinType] * Coin.weight
        return weight

    # check if a coin dictionary is valid
    def isValid(coins: dict):
        for coinType in Coin.EMPTY:
            if not coinType in coins:
                return False
        return True

    # add coins to a coins dictionary
    # returns false is the coins dict is not valid
    def addTo(self, coins: dict):
        if not Coin.isValid(coins):
            return False

        coins[self.type] += self.amount
        return True
