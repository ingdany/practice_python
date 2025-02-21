# syntax
tpl = ("item1", "item2", "item3")
len(tpl)

tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]


fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[0]
second_fruit = fruits[1]
print(first_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[las_index]


fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')

tpl = ("item1", "item2", "item3", "item4")
print("item2" in tpl)  # True


fruits = ("banana", "orange", "mango", "lemon")
# print("orange" in fruits)  # True
# print("apple" in fruits)  # False
print(fruits[1:])

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[1:])  # ['banana', 'orange']

fruits = ("banana", "orange", "mango", "lemon")
print(fruits)
del fruits
print(fruits)
