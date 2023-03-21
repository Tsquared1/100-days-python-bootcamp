from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n2 == 0:
        return "Dividing with 0 is not possible. Give another number."
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    next_calculation = True
    while next_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, "
                       f"or type 'x' to exit: ").lower()
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            next_calculation = False
            calculator()
        else:
            next_calculation = False






