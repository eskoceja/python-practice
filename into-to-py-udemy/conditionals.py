# conditional statements

if 5 > 3:
    print("hello")
    

if 3< 2:
    print("hello")
else:
    print("condition was not true")


# else if
age = 16
if age <= 15:
    print("you are younger than 16")
elif age == 16:
    print("you are 16")
else:
    print("you are older than 16")


if age < 13:
    print("you are a child")
elif age >= 13 and age <= 18:
    print("you are a teenager")
else:
    print("you are an adult")


if 5 > 3 or 2 < 1:
    print("hi")