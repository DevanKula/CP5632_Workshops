print('Electricity bill estimator')

cents_per_kWh = float(input('Enter cents per kWh:'))
daily_use_in_kWh = float(input('Enter daily use in kWh:'))
billing_days = float(input('Enter number of billing days:'))

estimated_bill = (cents_per_kWh * daily_use_in_kWh * billing_days) / 100

print("Estimated bill: ${:.2f}".format(estimated_bill))
