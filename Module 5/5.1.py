largest = None
smallest = None
avg = None
range = None
count = 0
sum = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
        if largest is None or n > largest :
            largest = n
        elif smallest is None or smallest > n :
            smallest = n
        sum = sum + n
        count = count + 1
    except:
        print("Invalid input")
avg = sum / count
range = (int(largest) - int(smallest) + 1)

print("Average is", avg)
print("Range is", range)
print("Count is", count)
