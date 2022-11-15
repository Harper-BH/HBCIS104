##if the text file only contained the word from, the program would fail

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 3: continue
    if words[0] != 'From' : continue
    print words[2]
