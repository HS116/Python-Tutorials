
#using "with" will automatically close the file
#make sure to specify mode e.g. read or write mode etc
with open("fileIO.txt", "w") as f:
    # "write" will override everything already in the file before !!!
    f.write("Edit\nEdit2\nEdit3")

with open("fileIO.txt", "r") as f:
    text = f.read()
    print(text)

#printing line by line

with open("fileIO.txt", "r") as f:
    text = f.read()
    for line in text:
        print(line, end = "")

#another method, best!
with open("fileIO.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

#append mode, does not overwrite the file content
with open("fileIO.txt", "a") as f:
    f.write("\nAppend")
