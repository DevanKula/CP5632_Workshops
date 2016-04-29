COLORS = {"coral":"#ff7f50", "coral1":"#ff7256", "coral2":"#ee6a50", "coral3":"#cd5b45", "coral4":"#8b3e2f", "CornflowerBlue":"#6495ed",
            "cornsilk1":"#fff8dc", "cornsilk2":"#eee8cd", "cornsilk3":"#cdc8b1", "cornsilk4":"#8b8878"}

color = input("Enter color: ").lower()
while color != "":
    if color in COLORS:
        print(color, "is", COLORS[color])
    else:
        print("Invalid color")
    color = input("Enter short color: ").lower()