# name = input("Enter name: ")
# print("(H)ello")
# print("(G)oodbye")
# print("(Q)uit")
# choice = input().upper()
# while choice != "Q":
#     if choice == "H":
#         print("Hello", name)
#     elif choice == "G":
#         print("Goodbye", name)
#     else:
#         print("Invalid choice")
#     print("(H)ello")
#     print("(G)oodbye")
#     print("(Q)uit")
#     choice = input().upper()
# print("Finished")

name = input("Enter name: ")
MENU = "(H)ello\n(G)oodbye\n(Q)uit  "
print(MENU)
choice = input(">>>").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello {}".format(name))
    elif choice == 'G':
        print("Goodbye {}".format(name))
    else:
        print("Invalid Choice")
    print(MENU)
    choice = input(">>>").upper()
print("Finished")