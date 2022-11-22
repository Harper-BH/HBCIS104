days = dict()
fname = input("Enter File:")
if len(fname) < 1:
    fname = ("mbox-short.txt")
file = open(fname)
for line in file:
    text = file.readlines()
    if line.startswith("From"):
        words = line.split()
        day = words[3]
        if day in days:
            days[day] = 1
        else:
            days[day] = days[day] + 1
    else: continue
print(days)
##not done
