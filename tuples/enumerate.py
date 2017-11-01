enum = (enumerate("abc"))
print(enum)

for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1, letter))