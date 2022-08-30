#optional/default parameters have a "default" value, which is set if no specific value is passed in e.g. below
#Rule: optional parameters should be after the normal parameters
def func(x, y = 5):
    print("x is " + str(x))
    print("y is " + str(y))

func(3)
func(3,4)


#can also pass in a keyword argument, when there are multiple optional params and u wanna single out a particular optional param
def func2(x = 6, y = 9):
    print("x is " + str(x))
    print("y is " + str(y))
func2(y=8)
