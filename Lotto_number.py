import random

#print(random.randint(5, 20))
#print(random.randrange(3, 10 ,2))
#print(random.uniform(2.5,5.5))

lotto_numbers = []
picks = int((input("How many quick picks?")))

for pick in range(picks):
    #lotto_numbers.append(pick)
    print(random.randrange(1,45,picks))