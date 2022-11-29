emails = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        email = words[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1
lst = list()
for k, v in emails.items():
    lst.append((v, k))
lst = sorted(lst, reverse=True)
lst2 = [(k, v) for v, k in lst]
for k, v in lst2:
    print(k, v)
    break
