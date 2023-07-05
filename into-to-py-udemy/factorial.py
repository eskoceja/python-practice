
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

result = calculate_factorial(5)
print(result)
# prints 120