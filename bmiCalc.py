print("Body-mass-index calculator, by Jason")

weight = float(input("Please enter your weight in kgs:"))
height = float(input("Please enter your height in m:"))

body_mass_index = weight / (height * height)

print('Therefore, your BMI value is:', body_mass_index)
print('Thank you!')
