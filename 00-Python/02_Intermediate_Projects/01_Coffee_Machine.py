
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
profit = 0


def is_resources_sufficient(coffe_name):
    ingredients = MENU[coffe_name]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry not enough {item}, in machine.")
            return False
    return True


def money(coffee_name):
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))

    total = (quarters * q) + (dimes * d) + (nickles * n) + (pennies * p)
    change = total - MENU[coffee_name]["cost"]

    if total < MENU[coffee_name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False

    else:
        print(f"Here is ${change:.2f} in change.")
        return True


def make_coffee(coffee_name):
    ingredients = MENU[coffee_name]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


Coffee_machine_off = True
while Coffee_machine_off:
    User_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if User_input == "off":
        Coffee_machine_off = False

    elif User_input == "report":
        print("Resources left: ")
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Profit: ${profit}")

    elif User_input in MENU:
        if is_resources_sufficient(User_input):
            if money(User_input):
                make_coffee(User_input)
                profit += MENU[User_input]["cost"]