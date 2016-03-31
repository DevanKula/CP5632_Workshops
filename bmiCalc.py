print("Body-mass-index calculator")

def main():
    weight = float(input("Please enter your weight in kgs:"))
    height = float(input("Please enter your height in m:"))
    print('Therefore, your BMI value is: {:,.2f}'.format(calculating_BMI(weight,height)))
    print('Thank you!')

def calculating_BMI(weight,height):
    return weight / (height * height)

main()