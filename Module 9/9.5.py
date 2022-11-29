domains = dict()

name = input('Enter file name: ')
if len(name) < 2:
    name = 'mbox-short.txt'
handle = open(name)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        at = words[1].find('@')
        domain = words[1][at+1:]
        if domain not in domains:
            domains[domain] = 1
        else:
            domains[domain] += 1

print(domains)
