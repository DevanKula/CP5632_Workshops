from car import Car


def main():
    limo = Car(100)
    limo.fuel += 20
    #print("Fuel =", limo.fuel)
    limo.drive(115)
    print(limo)
    #print("Odo =" ,limo.odometer)
    #print(limo)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)


main()
