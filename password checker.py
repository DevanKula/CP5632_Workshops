MAX_PASSWORD_LENGTH = 15
MIN_PASSWORD_LENGTH = 10
SPECIAL_CHARACTER = "!@#$%^&*()_-=+`~,./'<>?{}|"
MENU = "Please enter valid password \n Your must word msut be between 5 and 15 characters, and contain: \n 1 or more uppercase characters \n 1 or more lowercase characters \n 1 or more numbers \n and 1 or more special characters: !@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
print(MENU)

password = input()
lowers = 0
highers = 0
specials = 0
numbers = 0

for c in password:
    if c.islower():
        lowers += 1
    elif c.isupper():
        highers += 1
    elif c.isdigit():
        numbers += 1
    elif c in SPECIAL_CHARACTER:
        specials += 1

while lowers < 1 or highers < 1 or 1 < numbers or 1 < specials or len(password) < MIN_PASSWORD_LENGTH or len(password)> MAX_PASSWORD_LENGTH:
    print("Invalid password!")
    print(lowers,numbers,specials,highers)
    password = input()
else:
    print("Your",len(password), "character password is valid:", password)