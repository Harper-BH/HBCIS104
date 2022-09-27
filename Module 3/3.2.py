
sh = input("Enter Hours")
sr = input("Enter Rate")
try:
    fh = float(sh)
    fr = float(sr)
    if fh > 40.0 :
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        fp = otp + reg
    print (fp)
except:
    print("put a number")
