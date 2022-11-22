avg = None
total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        count = float(count) + 1
        total = total + float(line[21:30])
        avg = total / count
print("Average spam confidence:", avg)
