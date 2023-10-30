#weekly payroll


employeeName = input('What is your name? ')
hoursWorked = input('How many hours did you work this week? ')
hoursWorked = float(hoursWorked)
payRate = float(input('Enter pay rate '))

####if hoursWorked <= 40: ### if 40 >= hoursWorked:
    #### totalPay = hoursWorked * payRate
####if hoursWorked > 40:
    #### totalPay = payRate * 40 + ((hoursWorked - 40) * ((payRate * 1.5) + payRate))

if hoursWorked <= 40: ### This is a better option.....
    totalPay = hoursWorked * payRate
else:
    totalPay = payRate * 40 + ((hoursWorked - 40) * ((payRate * 1.5) + payRate))

### totalPay = hoursWorked * payRate
### totalPay = payRate * 40 + ((hoursWorked - 40) * (payRate * 1.5))

print('Weekly pay is $', format(totalPay, '1.2f'))
