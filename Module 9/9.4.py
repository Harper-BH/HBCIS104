numberlist = list()
people = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    text = handle.readlines()
    if line.startswith("From"):
        words = line.split()
        email = words[1]
        if email not in people:
            people[email] = .5
        else:
            people[email] = people[email] + .5
    else:
        continue
    numberlist.append(people[email])
    biggest = max(numberlist)
print(email, int(biggest))
