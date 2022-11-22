name = input("Enter file name: ")
file = open(name)
for line in file:
    print(line.upper)
print(file.upper)
