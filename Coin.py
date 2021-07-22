import traceback
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

# validations
if __name__ == "__main__":
    try:
        coins = {Coin.PLATINUM: 10, Coin.SILVER: 10, Coin.GOLD: 0, Coin.ELECTRUM: 0, Coin.COPPER: 0}
        coin = Coin(Coin.ELECTRUM, 5)
        coin.addTo(coins)
        if not coins == {Coin.PLATINUM: 10, Coin.SILVER: 10, Coin.GOLD: 0, Coin.ELECTRUM: 5, Coin.COPPER: 0}:
            print("ERROR: Coin addition broken")
        if not Coin.isValid(coins):
            print("ERROR: Coin validation is broken on all")
        if {Coin.PLATINUM, Coin.SILVER, Coin.GOLD, Coin.ELECTRUM, Coin.COPPER} != Coin.EMPTY:
            print("ERROR: Coin type list broken")
        if not Coin.isValid(Coin.EMPTY):
            print("ERROR: Coin validation is broken on empty")
    except Exception as e:
        # print a traceback
        print("Exception raised during inventory test: " + e)
        traceback.print_exc()