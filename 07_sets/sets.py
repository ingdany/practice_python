# syntax
st = {"item1", "item2", "item3", "item4"}
print(len(st))

st = {"item1", "item2", "item3", "item4", "item1"}
print(st)

# syntax
st = {"item1", "item2", "item3", "item4"}
print("Does set st contain item3? ", "item3" in st)  # Does set st contain item3? True


fruits = {"banana", "orange", "mango", "lemon"}
print("mango" in fruits)  # True


# syntax
st = {"item1", "item2", "item3", "item4"}
st.add("item5")
print(st)  # {'item1', 'item2', 'item3', 'item4', 'item5'}


fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
print(fruits)  # {'banana', 'orange', 'mango', 'lemon', 'lime'}

# syntax
st = {"item1", "item2", "item3", "item4"}
print(st)
st.update(["item5", "item6", "item7", "item2"])
print(st)


# syntax
st = {"item1", "item2", "item3", "item4"}
st.remove("item2")
print(st)  # {'item1', 'item3', 'item4'}

fruits = {"banana", "orange", "mango", "lemon"}
fruits.pop()  # removes a random item from the set
print(fruits)  # {'orange', 'mango', 'lemon'}


# syntax
st = {"item1", "item2", "item3", "item4"}
st.clear()
print(st)


fruits = {"banana", "orange", "mango", "lemon"}
del fruits
print(fruits)


# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st3 = st1.union(st2)
print(st3)


# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item3", "item2"}
st1.intersection(st2)  # {'item3', 'item2'}
print(st1)

# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True
print(st2)
print(st1)


# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2
print(st1)
print(st2)

# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1)  # {'item1', 'item4'}
print(st2)


# syntax
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
st2.isdisjoint(st1)  # False
print(st2)