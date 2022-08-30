'''
Containers are a data type that holds other objects 
e.g. lists, tuples, dictionaries, sets, etc
'''

import collections
'''
In the collections modules, there are so more data types 
e.g. counter, deque, namedTuple(), orderedDict, defaultdict
'''

from collections import Counter
# u can pass in any iterable/container as an arg below e.g. string, lists, tuples, etc
a = Counter("hello")
print(a)
b = Counter(["a", "b", "c"])
print(b)
c = Counter({"a" : 2, "b" : 5, "c" : 4})
print(c)
#u can also pass in key word arguments
d = Counter(cats = 4, dogs = 7)
print(d)
#returns the value 4 as declared above
print(d["cats"])
#returns 0, since not declared above
print(d["bird"])

#useful method to see all the elements in the counter e.g. if cats = 4, we will return the 4 "cats"
print(list(d.elements()))

#most useful method, "1" tells Python to look for the 1st most common element.
#  "2" would tell Python to look for the 2  most common elements
#Returns this element(s) and its/their count
print(d.most_common(1))
print(c.most_common(2))


#there are some additional methods e.g. .subtract() and .update(). 
# Also you can do intersection (&) of counters and union (|) of counters
#u can also do regaular addition (+) and subtraction (-) of counters
