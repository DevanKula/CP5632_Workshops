input_one = int(input("Enter lowest number: "))
input_two = int(input("Enter highest number: "))
print("1. Show the even numbers from {} to {}".format(input_one, input_two))
print("2. Show the odd numbers from {} to {}".format(input_one, input_two))
print("3. Show the squares from {} to {}".format(input_one, input_two))
print("4. Exit program")
choice = input("Enter option: ")
while choice != "4":
    if choice == "1":
        for i in range(input_one, input_two + 1, 1):
            if (i % 2) == 0:
                print(i, sep='\n')
    elif choice == "2":
        for i in range(input_one, input_two + 1, 1):
            if (i % 2) != 0:
                print(i, sep='\n')
    elif choice == "3":
        for i in range(input_one, input_two + 1, 1):
            print(i * i, sep='\n')
    else:
        print("Invalid Choice")
    print()
    input_one = int(input("Enter lowest number: "))
    input_two = int(input("Enter highest number: "))
    print("1. Show the even numbers from {} to {}".format(input_one, input_two))
    print("2. Show the odd numbers from {} to {}".format(input_one, input_two))
    print("3. Show the squares from {} to {}".format(input_one, input_two))
    print("4. Exit program")
    choice = input("Enter option: ")
