logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2 if n2 != 0 else "Cannot divide by zero"


operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}
# print(operations["*"](10,2)) Output: 20

def calculator():
    print(logo)
    first_number = float(input("What is the first number?: "))
    game_over = True

    while game_over:

        for symbol in operations:
            print(symbol)
        math_operators = input("Pick an operation: ")

        next_number = float(input("What is the next number?: "))

        ans = (f"{first_number} {math_operators} {next_number} = {operations[math_operators](first_number, next_number)}")
        print(ans)
        continue_with_previous_result = input(f"Type 'y' to continue calculating with {ans} or Type 'n' to start a new calculation: ").lower()

        if continue_with_previous_result == "y":
            ans = first_number
        else:
            game_over = False
            print("\n"* 200)
            calculator()

calculator()
