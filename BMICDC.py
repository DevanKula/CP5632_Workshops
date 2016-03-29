print("Body-mass-index calculator, by Jason")

weight = float(input("Please enter your weight in kgs:"))
height = float(input("Please enter your height in m:"))

body_mass_index = weight / (height * height)
if body_mass_index < 18.5:
    print('Therefore, your BMI value is:', body_mass_index)
    print("Weight status: Underweight")
elif 18.5 >= body_mass_index <= 24.9:
    print('Therefore, your BMI value is:', body_mass_index)
    print("Weight status: Normal")
elif 25.0 >= body_mass_index <= 29.9:
    print('Therefore, your BMI value is:', body_mass_index)
    print("Weight status: Overweight")
elif body_mass_index >= 30:
    print('Therefore, your BMI value is:', body_mass_index)
    print("Weight status: Obese")
print('Thank you!')
