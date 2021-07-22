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

# if name is main test the class
if __name__ == "__main__":
    c = Coin(Coin.PLATINUM, 1)
    print(c.getCoinWeight(Coin.EMPTY))