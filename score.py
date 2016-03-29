score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50:
        print("Bad")
    elif score < 89:
        print("Passable")
    else:
        print("Excellent")


