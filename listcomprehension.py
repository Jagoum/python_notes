friuits = ["apple", "banana", "grapes", "lime", "kiri", "lemon", "pepper", "cherry"]
mylist = [item for item in friuits if "a" in item]
print(mylist)
not_apple = [fruits for fruits in friuits if fruits != "apple" and fruits !="banana"]
print(not_apple)
squares = [x**2 for x in range(1,10)]
print(squares)
even_or_odd = ["Even" if x%2 == 0 else "Odd" for x in range(10)]
print(even_or_odd)
even_only = [x for x in range(1,10) if x % 2 == 0 ]
print(even_only)