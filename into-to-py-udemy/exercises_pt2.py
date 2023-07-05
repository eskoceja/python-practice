# Lists, dictionaries, tuples

# 1. create ist of names and print the second item
items = ['goat', 'cow', 'horse', 'chicken']
print(items[1])

# 2. create list of sports and replace second item with another sport
sports = ['volleyball', 'football', 'baseball', 'soccer', 'basketball']
sports[1] = 'golf'
print(sports)

# 3. create list containing numbers and delete the fifth number from the array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[4]
print(numbers)

# 4. create 2 lists of numbers and merge them
numbers2 = [10, 11, 12, 13, 14, 15]
merged = numbers + numbers2
print(merged)

# 5. create a list of numbers and find length, min, and max
print(min(merged))
print(max(merged))

# 6. create dictionary of students and scores and print scores
students = {
    'shrek': 89,
    'fiona': 100,
    'donkey': 96
}
print(students.values())

# 7. create dictionary with key being names and values being ages and delete the second key/value pair
del students['fiona']
print(students)

# 8. create dictionary of names and ages and print all keys and values
print(students.keys())
print(students.values())

# 9. create tuple of fav movies
movies = ("jane eyre", "zootopia", "moana", "inside out", "brave")
print(movies)

# 10. create a tuple and print all items from the 1st to 3rd index
print(movies[0:3])