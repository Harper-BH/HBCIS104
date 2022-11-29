import re
sum = 0
lst = list()
name = input('File name:')
if len(name) < 2:
    name = 'regex_sum_42.txt'
hand = open(name)
for line in hand:
    nums = re.findall('[0-9]+',line)
    lst.append(nums)
for num in lst:
    sum = sum + num
print(sum)
