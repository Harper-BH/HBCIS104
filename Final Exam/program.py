avg = 0
count = 0
total = 0
lst = list()
while True:
    ##asks for a number over and over again
    inp = input('Enter a Number:')
    if inp == 'quit':
        break
    try:
        ##checks if the number is an integer, if it is it adds it to the list
        number = int(inp)
        lst.append(number)
    except:
        ##handles non integers
        print('Invalid Input')
for num in lst:
    #adding up total and count
    total = int(total) + int(num)
    count = int(count) + 1
avg = total / count
print('Total is:', total, 'Count is:', count, 'Average is:', avg)
