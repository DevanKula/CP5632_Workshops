print("Temperature Conversion Program")

celsiusValue = float(input("Enter celsius value: "))
fahrenheitValue = celsiusValue * 9 / 5 + 32
kelvinValue = 5 / 9 * (fahrenheitValue - 32) + 273

print("Celsius value:", celsiusValue)
print("Fahrenheit value:", fahrenheitValue)
print('Kelvin value:', kelvinValue)
