from guitar import Guitar

def main():
    print("My guitars!")
    name = input("Name: ")
    gibson = []
    while name != "":
        year = int(input("Year: "))
        cost = input("Cost: $")
        gibson.append(Guitar(name, year, cost))
        name = input("Name: ")
    else:
        counter = 0

        print("\nThese are my guitars: ")
        for test in gibson:
            counter += 1
            print("Guitar: " ,counter, test)
main()