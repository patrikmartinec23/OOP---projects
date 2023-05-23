# Import class CoffeeMachine
from brew import *
from fails import *

# Create object
oCoffe = CoffeeMachine(resources.get('water'), resources.get('milk'), resources.get('coffee'))

# Infinite loop
while True:
    print()
    action = input('What would you like? (espresso/latte/cappuccino): ').lower()

    try:
        if action == 'espresso':
            oCoffe.espresso()

        if action == 'latte':
            oCoffe.latte()

        if action == 'cappuccino':
            oCoffe.cappuccino()

        if action == 'report':
            oCoffe.report()

        # Breaks the loop
        if action == 'off':
            break

    except AbortProcess as error:
        print(error)

print('shutting down')
