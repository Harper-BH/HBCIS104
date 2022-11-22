days = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    text = handle.readlines()
    if line.startswith("From"):
        words = line.split()
        day = words[1]
        if email not in people:
            people[email] = 1
        else:
            people[email] = people[email] + 1
    else:
        continue
print(people)
