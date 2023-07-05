def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "Error, cannot divide by 0"

print("\n --- Calculator --- \n ------------------ ")

while True:
    menu = """Select an operation 
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    0. End"""
    print(menu)

    choice = int(input("Enter your choice:\n"))

    if choice == 0:
        print("Good-bye!")
        break

    num1 = float(input("Enter a number:\n"))
    num2 = float(input("Enter another number:\n"))

    if choice == 1:
        addition = add(num1, num2)
        print("The sum of", num1, "and", num2, "is", addition)
    elif choice == 2:
        difference = subtract(num1, num2)
        print("The difference of", num1, "and", num2, "is", difference)
    elif choice == 3:
        product = multiply(num1, num2)
        print("The product of", num1, "and", num2, "is", product)
    elif choice == 4:
        quotient = divide(num1, num2)
        print("The quotient of", num1, "and", num2, "is", quotient)
    else:
        print("Invalid entry, try again!")
