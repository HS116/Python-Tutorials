#REMEM for all these methods, strings are immutable, hence the method will return a new string
#and not modify the string in place

#.strip() removes only all the trailing and leading whitspaces in the string

word1 = "          Hello my name is Neil          "
print(word1.strip())

#len() is a function, NOT a method
print(len(word1))

print(word1.lower())


print(word1.upper())


#split() create a list from the string. Takes in a delimiter, which is what u wanna split by. Default is space. 
#The delimeter is not included in the list e.g. in below example space is not included
print(word1.split())
print(word1.split("e"))
print(word1.split("m"))