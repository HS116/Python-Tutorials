
old_list = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x ** x


#Without map()
print("Using old way: ")
new_list = []
for elem in old_list:
    new_list.append(func(elem))

print(new_list)
print("\n")


#Way Better way with map(). 
#remem map() return a map object, to convert the map obj into a list we can use list()
print("Using map(): ")
print(list(map(func, old_list)))
print("\n")

#Another alternative: list comprehension, including the twist with the if statement (only even x) inside
print("Using list comprehension: ")
print([func(x) for x in old_list if x % 2 == 0])


