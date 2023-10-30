cost = float (input ('Enter cost of the product ')) ### 3.37
amountPaid = float (input('Enter amount offered ')) ### 5.00

if amountPaid >= cost:
    change = amountPaid - cost
    dollars = int(change)
    change = change - dollars
    change = round (change * 100)
    
    quarters = change // 25 ### or do this: quarters = int (change/25)
    change = change - quarters * 25  ### or change = change % 25
    
    dimes = change // 10 ### or do this: dimes = int (change/25)
    change = change - dimes * 10
    
    nickels = change // 5
    pennies = change - nickels * 5
    
    print ()
    if dollars > 0:
        print ('Dollars ', dollars)
    if quarters > 0:
        print ('Quarters', quarters)
    if dimes > 0:
        print ('Dimes   ', dimes)
    if nickels > 0:
        print ('Nickles ', nickels)
    if pennies > 0:
        print ('Pennies ', pennies)
    
else:
    
    print ('Need more money!')
