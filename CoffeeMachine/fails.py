class AbortProcess(Exception):
    """Raise this exception to abort a coffe brew"""
    pass


class Validate(object):

    def __init__(self, inserted_coins, cost):
        self.inserted_coins = float(inserted_coins)
        self.cost = float(cost)

    # Checks if enough money was put in otherwise It stops
    def check_money(self):

        if self.inserted_coins == self.cost:
            pass

        elif self.inserted_coins >= self.cost:
            print(f'Here is ${self.inserted_coins - self.cost} in change.')

        else:
            raise AbortProcess("Sorry that's not enough money. Money refunded.")




