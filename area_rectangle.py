
def main():
    length = float(input("Enter Length(cm): "))
    width = float(input("Enter width(cm): "))
    print("The area is {:,.2f} sqcm".format(calculate_area(length,width)))

def calculate_area(length, width):
    return length * width

main()