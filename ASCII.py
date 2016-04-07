<<<<<<< HEAD
#lower = 10
#upper = 100
for i in range(10, 120, 11):
    print("{}{}".format(i, chr(i)))
#print("Enter a number ({} - {})".format(lower,upper))
#input()
=======
lower = 10
upper = 50

#print("Enter a number (" +str(lower) + "-" + str(upper) + "):")
#print("Enter a number ({}-{}):".format(lower,upper).strip())
def main():
    for i in range(get_number(upper,lower), 120, 11):
        print("{}{:>15}".format(i, chr(i)).strip())



def get_number(upper, lower):
    number = int(input("Enter a number ({}-{}):".format(lower,upper)))
    while 10 > number or 50 < number:
        print("Enter valid number!")
        number = int(input("Enter a number ({}-{}):".format(lower,upper)))
    else:
        return number
main()
>>>>>>> origin/master
