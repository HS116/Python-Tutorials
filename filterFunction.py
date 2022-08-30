def add7(x):
    return x+7

def isOdd(x):
    return x % 2 == 1

a = [1,2,3,4,5,6,7,8,9,10]

#old traditional way without filter() or list comprehension
b = []
for elem in a:
    if isOdd(elem):
        b.append(elem)
print(b)

#better way with filter()
#remem filter() return a filter object, which can be converted to a list using list() 
c = list(filter(isOdd, a))
print(c)

#using map() with filter()
# remem map() needs an iterable and a filter object will serve this purpose just fine
d = list(map(add7, filter(isOdd, a)))
print(d)


#another alternative: list comprehension
e = [x for x in a if isOdd(x)]
print(e)