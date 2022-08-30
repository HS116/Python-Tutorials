#global variables can be accessed from anywhere in the program
#but local variables can only be accesses within the particular function or area of code


#this is a global "var"
var = 5

def func():
    #this is a local "var", which is completely different to the above global "var"
    var = 4
    print("Local: " + str(var))

func()
#which is why the value of the global "var" does not change
print("Global: " + str(var))

def func2():
    #in order to change the global "var" from within a function, we do the following:
    global var 
    var = 8
    print ("Local: " + str(var))

func2()
print("Global: " + str(var))

#more practise


num = 20

def increm1():
    num = 5
    num += 1
    print("Local num: " + str(num))

def increm2():
    global num
    num += 1
    print("Local num: " + str(num))

increm1()
increm2()
print("Global num: " + str(num))


