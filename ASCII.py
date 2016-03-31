#lower = 10
#upper = 100
#print("Enter a number (" +str(lower) + "-" + str(upper) + "):")
#print("Enter a number ({}-{}):".format(lower,upper).strip())

for i in range(10, 120, 11):
    print("{}{:>15}".format(i, chr(i)).strip())