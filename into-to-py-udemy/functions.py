# Functions!

# A baker makes Emily's special break
# Series of steps: mix, knead, rise, bake
# make_special_break() performs these steps

def hello_world():
    print("Hello World!")


hello_world()


def greeting(name):
    print("Hi " + name + "!")


greeting("Emily")


def add(num1, num2):
    print(num1 + num2)


add(10, 15)


def add_again(num1, num2):
    return num1 + num2


num_sum = add_again(12, 34)
print(num_sum)


def mul(num1, num2):
    return num1 * num2

print(mul(add_again(1, 2), add_again(3, 4)))