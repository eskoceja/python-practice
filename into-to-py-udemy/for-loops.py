# intro to for loops

list1 = ['apples', 'bananas', 'cherries']
for item in list1:
    print(item)


tup1 = (2, 6, 10)
for item in tup1:
    print(item)


for i in range(0, 10):
    print(i)

# prints even numbers from 0-10 (2 is the increment factor)
for i in range(0, 11, 2):
    print(i)

# print first 10 multiples of 5
for i in range(0, 51, 5):
    print(i)

# nested for loops
for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)
