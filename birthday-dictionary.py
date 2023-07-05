if __name__ == '__main__':
    birthdays = {
        "Dolores Huerta": "4/10/1940",
        "Ellen Ochoa": "5/10/1958",
        "Sylvia Rivera": "6/2/1951",
        "Rigoberta Menchu": "1/9/1959",
        "Berta Caceras": "3/4/1971",
        "Carmen Miranda": "2/9/1909",
        "Frida Kahlo": "7/6/1907"
    }

    print("Welcome to the birthday dictionary! We have the birthdays of:\n")
    for name in birthdays:
        print(name)

    while True:
        print("\nWho's birthday would you like to look up?")
        name = input()
        if name == "quit":
            break

        if name in birthdays:
            print('{}\'s birthday is {}.'.format(name, birthdays[name]))
        else:
            print('Sadly, we don\'t have {}\'s birthday.'.format(name))
