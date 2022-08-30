'''
Main use cases:
1.) mini functions that do not really require a name
2.) in map() or filter()
3.) sometimes a mini function that is only being used within a particular function
'''

func1 = lambda x : x+2
print(func1(5))

#Use Case 3 (mini function only being used within another particular function):
def func2(x):
    func3 = lambda x : x*3
    return 3 + func3(x)

print(func2(5))

#lambda functions can still have multiple parameters and optional parameters as well
func4 = lambda x, y = 1 : x * y
print(func4(3))
print(func4(3,5))

a = [1,2,3,4,5,6,7,8,9,10]

#Use Case 2: map() and filter()
plus8_list = list(map(lambda x : x + 8, a))
print(plus8_list)

even_list = list(filter(lambda x : x % 2 == 0, a))
print(even_list)

even_plus8_list = list(map(lambda x : x + 8, filter(lambda x : x % 2 == 0, a)))
print(even_plus8_list)