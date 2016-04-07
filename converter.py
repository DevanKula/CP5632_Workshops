print("Temperature Conversion Program")

def main():
    celsiusValue = float(input("Enter celsius value: "))
    print("Fahrenheit value:", convert_celsius_to_fahrenheit(celsiusValue))

def convert_celsius_to_fahrenheit(value):
     return value * 9 / 5 + 32
main()



#kelvinValue = 5 / 9 * (fahrenheitValue - 32) + 273

#print("Celsius value:", celsiusValue)
#print("Fahrenheit value:", fahrenheitValue)
#print('Kelvin value:', kelvinValue)
