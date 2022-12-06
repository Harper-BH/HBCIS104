import re
count = 0
exp = input('Enter a regular expression: ')
str_exp = str(exp)
fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if re.findall(str_exp, line) != []:
        count += 1
print(fname, ' had ', str(count), ' lines that matched ', str_exp)
