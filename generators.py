#Generators are a bit like iterators
#They allow us to load in data one piece at a time
#Hence better memory efficiency
#Especially useful when trying to load in a very large file
#cuz we're only keeping track of the "next" element. We're not storing the previous or future next elements. 


#Traditional way
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    #dunder method allows us to do next(g) as seen below
    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration
        else: 
            return_value = self.last ** 2
            self.last += 1
            return return_value

g = Gen(10)
while True:
    try:
        print(next(g))
    except StopIteration:
        break

#Better way using Python generator syntax!!!

def gen(n):
    for i in range(n):
        #"yield" is kinda like a pause of the function to yield the next element
        #whereas "return" is like a stop of the function
        yield i**2

g = gen(10)
for i in g:
    print(i)

print(next(g))
            
#Corey Schafer ...

