print('Electricity Bill Estimator 2.0')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = float(input('Which Tariff? 11 or 31:'))
while tariff == 11 and 31:
    daily_use_in_kWh = float(input('Enter daily use in kWh:'))
    billing_days = float(input('Enter number of billing days:'))
    if tariff == 11:
        estimated_bill = (TARIFF_11 * daily_use_in_kWh * billing_days)
        print('Estimated bill: ${:.2f}'.format(estimated_bill))
    elif tariff == 31:
        estimated_bill = (TARIFF_31 * daily_use_in_kWh * billing_days)
        print('Estimated bill: ${:.2f}'.format(estimated_bill))
    break

