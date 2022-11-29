people = dict()
name = input('Enter file:')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in people:
            people[words[1]] = 1
        else:
            people[words[1]] += 1

print(people)
