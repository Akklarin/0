msg = "Hello world!"
file = open("newfile.txt", "w")
a = file.write(msg)
print(a)
file.close()

file = open("newfile.txt", "r")
print(file.read())