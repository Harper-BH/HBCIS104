g = input("Input Grade")
try:
    g = float(g)
    if g < 0.0 or g > 1.0:
        print("error")
    elif g >= 0.9:
        print("A")
    elif g >= 0.8:
        print("B")
    elif g >= 0.7:
        print("C")
    elif g >= 0.6:
        print("D")
    elif g < 0.6:
        print("F")
except:
    print("Put a Number")
