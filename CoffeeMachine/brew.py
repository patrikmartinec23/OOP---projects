from menu import *
from fails import *


class CoffeeMachine(object):

    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0

    def report(self):
        print("Water: ", self.water, "ml", sep="")
        print("Milk: ", self.milk, "ml", sep="")
        print("Coffee: ", self.coffee, "g", sep="")
        print("Money: ""$", self.money, sep="")
        print()

    def get_money(self):  # Inserts money in machine
        print('Please insert coins')
        quarters = input("how many quarters?: ")
        dimes = input("How many dimes?: ")
        nickels = input("How many nickels?: ")
        pennies = input("How many pennies?: ")

        if quarters == "" or dimes == "" or nickels == "" or pennies == "":
            raise AbortProcess("Input error. Specify how many coins you put in.")

        else:
            quarters = float(quarters) * 0.25
            dimes = float(dimes) * 0.10
            nickels = float(nickels) * 0.05
            pennies = float(pennies) * 0.01
            return quarters + nickels + pennies + dimes


    def espresso(self):
        inserted_coins = self.get_money()
        self.water -= MENU["espresso"]['ingredients']["water"]
        self.coffee -= MENU["espresso"]['ingredients']["coffee"]
        if self.water >= 0 and self.coffee >= 0:
            cost = MENU["espresso"]['cost']
            self.water += MENU["espresso"]['ingredients']["water"]
            self.coffee += MENU["espresso"]['ingredients']["coffee"]
            check = Validate(inserted_coins, cost).check_money()
            print("Here is your espresso ☕️.Enjoy!")
            self.water -= MENU["espresso"]['ingredients']["water"]
            self.coffee -= MENU["espresso"]['ingredients']["coffee"]
            self.money += float(MENU["espresso"]['cost'])
        else:
            raise AbortProcess('resources are depleted')

    def latte(self):
        inserted_coins = self.get_money()
        self.water -= MENU["latte"]['ingredients']["water"]
        self.coffee -= MENU["latte"]['ingredients']["coffee"]
        self.milk -= MENU["latte"]['ingredients']["milk"]
        if self.water >= 0 and self.coffee >= 0 and self.milk >= 0:
            cost = MENU["espresso"]['cost']
            self.water += MENU["latte"]['ingredients']["water"]
            self.coffee += MENU["latte"]['ingredients']["coffee"]
            self.milk += MENU["latte"]['ingredients']["milk"]
            check = Validate(inserted_coins, cost).check_money()
            self.water -= MENU["latte"]['ingredients']["water"]
            self.coffee -= MENU["latte"]['ingredients']["coffee"]
            self.milk -= MENU["latte"]['ingredients']["milk"]
            print("Here is your latte ☕️.Enjoy!")
            self.money += float(MENU["latte"]['cost'])
        else:
            raise AbortProcess('resources are depleted')

    def cappuccino(self):
        inserted_coins = self.get_money()
        self.water -= MENU["cappuccino"]['ingredients']["water"]
        self.coffee -= MENU["cappuccino"]['ingredients']["coffee"]
        self.milk -= MENU["cappuccino"]['ingredients']["milk"]
        if self.water >= 0 and self.coffee >= 0 and self.milk >= 0:
            cost = MENU["espresso"]['cost']
            self.water += MENU["cappuccino"]['ingredients']["water"]
            self.coffee += MENU["cappuccino"]['ingredients']["coffee"]
            self.milk += MENU["cappuccino"]['ingredients']["milk"]
            check = Validate(inserted_coins, cost).check_money()
            self.water -= MENU["cappuccino"]['ingredients']["water"]
            self.coffee -= MENU["cappuccino"]['ingredients']["coffee"]
            self.milk -= MENU["cappuccino"]['ingredients']["milk"]
            print("Here is your cappuccino ☕️.Enjoy!")
            self.money += float(MENU["cappuccino"]['cost'])
        else:
            raise AbortProcess('resources are depleted')
