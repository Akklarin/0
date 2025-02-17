file = open("spis.txt", "r")
for line in file:
    if "\n" in line:
        lenOfLine = str(len(line) - 1)
    else:
        lenOfLine = str(len(line))
    print(line[0] + lenOfLine)
file.close()
