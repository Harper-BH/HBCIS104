import re
sum = 0
count = 0
lst = list()
name = input('File name:')
if len(name) < 2:
    name = 'regex_sum_1648151.txt'
hand = open(name)
for line in hand:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    if len(nums) > 0:
        for number in nums:
            number = float(number)
            lst = lst + [number]
    else:
        continue
for num in lst:
    sum = float(sum) + float(num)
print(int(sum))
