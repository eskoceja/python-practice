# intro to lists
# ordered items, have index, know the order

shopping_list = ['apples', 'bananas', 'oranges', 'cheese']

print(shopping_list)
print(shopping_list[1])
print(shopping_list[0:2])

# add item to list
shopping_list.append('blueberries')
print(shopping_list)

# update item in list
shopping_list[0] = 'cherries'
print(shopping_list)

# delete item in list
del shopping_list[1]
print(shopping_list)

# how many items in list
print(len(shopping_list))

# join lists together
shopping_list2 = ['bread', 'jam', 'pb']
print(shopping_list + shopping_list2)

# repeat a list
print(shopping_list * 2)

# max and min
list_num = [1, 4, 7, 23, 6]
print(max(list_num))
print(min(list_num))