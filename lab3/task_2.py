from os import listdir

files = listdir("./lab3/")

for file in files:
    if file.split(".")[-1] == "py":
        print("\u001b[34m" + file + "\u001b[0m")
    else:
        print(file)
