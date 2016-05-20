from car import Car


def main():
    limo = Car(100)
    limo.fuel += 20
    limo.drive(115)
    print(limo)
main()
