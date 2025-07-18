Mark = float(input("Mark of the person:"))

if Mark >= 101:
    print("verify your mark")
    exit()

if Mark >= 90:
    print("Grade A")
elif Mark >= 80:
    print("Grade B")
elif Mark >= 70:
    print("Grade C")
elif Mark >= 60:
    print("Grade D")
else:
    print("Grade F")