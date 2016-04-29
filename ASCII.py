

#print("Enter a number (" +str(lower) + "-" + str(upper) + "):")
#print("Enter a number ({}-{}):".format(lower,upper).strip())
def main():
    get_number(10, 100)
    for i in range(10, 120, 11):
        print("{}{:>15}".format(i, chr(i)).strip())

def get_number(lower, upper):
    number = input("Enter a number ({}-{}):".format(lower,upper))
    while not number.isdecimal() or lower > int(number) or upper < int(number):
        print("Enter valid number!")
        number = input("Enter a number ({}-{}):".format(lower,upper))
    else:
        return number
main()
