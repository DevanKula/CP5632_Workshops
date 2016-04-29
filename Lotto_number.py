import random

picks = int(input("How many quick picks?"))

for pick in range(picks):
    lotto_numbers = []
    for i in range(6):
        new_num = random.randint(1,45)
        while new_num in lotto_numbers:
            new_num = random.randint(1,45)
        lotto_numbers.append(new_num)
        lotto_numbers.sort()
    for number in lotto_numbers:
        print("{:2}".format(number), end=' ')
    print()








#    lotto_numbers.append(random.randrange(1,45,1))
#    print(lotto_numbers)
#lotto_numbers = []
#picks = int((input("How many quick picks?")))

#for pick in range(picks):
#    print(random.randint(1,45))'''
