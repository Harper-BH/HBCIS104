people = dict()
maximum = 0
most_emails = ''

fname = input('Enter file name: ')
if len(fname) < 2:
    fname = 'mbox-short.txt'
handle = open(fname)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    if words[1] not in people:
        people[words[1]] = 1
    else:
        people[words[1]] += 1

for person in people:
    if people[person] > maximum:
        maximum = people[person]
        most_emails = person

print(most_emails, maximum)
