fileName = "fileIO_Practise_2.txt"
with open(fileName, "w") as f:
    f.write("Hello")

#appending
with open(fileName, "a") as f:
    f.write("\nEdit ")

with open(fileName, "r") as f:
    text = f.read()
    print(text)

with open(fileName, "r") as f:
    lines = f.readlines()
    for lineNumber in range(len(lines)):
        print("Line " + str(lineNumber + 1) + ": " + lines[lineNumber])

