hours = dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        time = words[5]
        colon = time.split(':')
        hour = colon[0]
        if hour not in hours:
            hours[hour] = 1
        else:
            hours[hour] += 1
for (k, v) in sorted(hours.items()):
    print(k, v)
