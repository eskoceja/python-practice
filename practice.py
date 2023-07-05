# 1. Character Input
name = input("What's your name?")
print("Hello " + name + "!")
# print(name * 2)

# 2. Odd or Even
# age = int(input("How old are you?"))
# if age < 13:
#     print("You are too young too see this movie")
# else:
#     print("Enjoy the movie!")

# num = int(input("Enter a number and I'll tell you if it's odd or even"))
# mod = num % 2

# if mod > 0:
#     print("You picked an odd number")
# else:
#     print("You picked an even number")

number = int(input("Enter a number for me to check: "))
check = int(input("Enter a number to divide by: "))
if number % 4 == 0:
    print(str(number) + " is a multiple of 4")
elif number % 2 == 0:
    print(str(number) + " is an even number")
else:
    print(str(number) + " is an odd number")

if number % check == 0:
    print(str(number) + " divides evenly by " + str(check))
else:
    print(str(number) + " does not divide evenly by " + str(check))

# 3. List less than ten
try:
    grade = int(input("Enter a grade between 0-100: "))
except ValueError:
    print("Invalid entry, try again")
else:
    if grade >= 90:
        print("A")
    elif grade >=80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

a = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 6, 9, 10, 11, 28, 29, 30]

# for x in a:
#     if x < 5:
#         print(x)

print([x for x in a if x < 5])

listOfNums = [7, 3, 8, 9, 13, 14, 15, 21, 23, 34, 45, 67]
lessFnums =[]
for nums in listOfNums:
    if nums < 5:
        lessFnums.append(nums)
        lessFnums.sort()
print(lessFnums)
print()

numbs = int(input("Enter a number: "))
for n in range(numbs):
    if n < numbs:
        lessFnums.append(n)
        lessFnums.sort()
print(lessFnums)

# 4. Divisors
# b = range(2, 11)
# for elem in b:
#     print(elem)

numero = int(input("Enter a number to get back divisors: "))
listRange = list(range(1, numero+1))
divisorList = []
for number in listRange:
    if numero % number == 0:
        divisorList.append(number)

print(divisorList)

# 5. List Overlap
e = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(e) & set(f))
print(common_elements)

# 6. String Lists
# wrd = input("Enter a word: ")
# wrd = str(wrd)
# rsv =wrd[::-1]
# print(rsv)
# if wrd == rsv:
#     print("This word is a palindrome")
# else: 
#     print("This word is not a palindrome")

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

word = input('enter a word:\n')
x = reverse(word)
if x == word:
    print("this is a palindrome")
else:
    print("this is not a palindrome")

# 7. List Comprehensions
years_of_birth = [1962, 1960, 1975, 1995, 1993]
# ages =[]
# for year in years_of_birth:
#     ages.append(2023 - year)
# print(ages)
ages = [2023 - year for year in years_of_birth]
print(ages)

m = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
o = [number for number in a if number % 2 == 0]

print(o)