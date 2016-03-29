try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers! ")
except ZeroDivisionError:
        print("Cannot divide by Zero!")
print("Finsihed")
