import random


def main():
    MAX_INCREASE = 0.1  # 10%
    MAX_DECREASE = 0.05 # 5%
    MIN_PRICE = 1.0
    MAX_PRICE = 100.0
    INITIAL_PRICE = 10.0
    day = 0
    price = INITIAL_PRICE
    print("Starting price {}".format(format_currency(price)))


    while MIN_PRICE <= price <= MAX_PRICE:
        priceChange = 0
        day += 1
        if random.randint(1, 2) == 1:
            priceChange = random.uniform(0, MAX_INCREASE)
        else:
            priceChange =  random.uniform(-MAX_DECREASE, 0)
        price *= (1 + priceChange)
        print("On day {} price is {}".format(day,format_currency(price)))


def format_currency(value):
    return '${:,.2f}'.format(value)
main()