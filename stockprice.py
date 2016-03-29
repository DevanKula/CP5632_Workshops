import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
day = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    priceChange = 0
    day += 1
    if random.randint(1, 2) == 1:
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        priceChange =  random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    print('On day {} price is ${:,.2f}'.format(day,price))
