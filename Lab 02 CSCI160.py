### Joshua W George - CSCI 160 Online - Lab 2 - joshua.w.george@ndus.edu

import math  ### math module was specified for part 4, but I used it elsewhere as well.

print ('Part 1')
print ('Converting hours, minutes, and seconds into total seconds.')

'''
Part 1 – Convert to seconds
1. Add a comment section to your program
2. Prompt the user to enter three integers for hours, minutes and seconds
3. Use variables with meaningful names
4. Calculate and display the number of equivalent seconds
'''

print ()
print () 
hours = int(input('Enter in the amount of hours ----> '))
minutes = int(input('Enter in the amount of minutes --> '))
seconds = int(input('Enter in the amount of seconds --> '))
totalSeconds = (hours * 3600) + (minutes * 60) + seconds
print ()
print ()
print ('Hours  :', hours)
print ('Minutes:', minutes)
print ('Seconds:', seconds)
print (math.ceil(totalSeconds), 'seconds total') ### I opted to round up on the seconds, because having a fraction of a second seems meaningless in this case.
print ()
print ('----------------------------------------------------------------')
print ()

print ('Part 2')
print ('Converting seconds into hours, minutes, and seconds.')

'''
Part 2 – Convert from seconds
1. Add a comment section to your program.
2. Prompt the user to enter one integer value, which will be the number of seconds
3. Calculate and display the number of equivalent hours, minutes and seconds
(refer to documentation and/or notes about integer division and the modulo or
remainder operator). The output should be on a single line.
'''

print ()
print () 
totalSeconds = int(input('Enter in the amount of seconds to covert ----> '))
hours = totalSeconds / 3600
minutes = (totalSeconds % 3600) / 60
seconds = (totalSeconds % 3600) % 60
print ()
print ()
print ('Seconds: ', totalSeconds, '\nThis is',int(hours),'hours,', int(minutes),'minutes and,', math.ceil(seconds),'seconds.') ### Again opted to round up. Also used \n for one output multiple lines.
print ()
print ('----------------------------------------------------------------')
print ()

print ('Part 3')
print ('Converting dollars to change.')

'''
Part 3 – Convert to dollars
1. Prompt the user to enter four integers: quarters, dimes, nickels and pennies.
2. Calculate the total number of cents
3. Convert from cents to dollars by dividing by 100.0
4. Display the equivalent in dollars and cents.
'''

print ()
print () 
quarters = int(input('Enter in the amount of quarters --> '))
dimes = int(input('Enter in the amount of dimes -----> '))
nickels = int(input('Enter in the amount of nickels ---> '))
pennies = int(input('Enter in the amount of pennies ---> '))
totalQuarters = quarters * 25 
totalDimes = dimes * 10
totalNickels = nickels * 5
totalPennies = pennies * 1
total = (totalQuarters + totalDimes + totalNickels + totalPennies) / 100.0  ### Convert from cents to dollars by dividing by 100.0
print ()
print ()
print ('Quarters:', quarters)
print ('Dimes:   ', dimes)
print ('Nickels: ', nickels)
print ('Pennies: ', pennies)
print ('This is equal to $', '{:.2f}'.format(total), sep='')  ### Used format and sep= to provide the proper look of the dollar amount. 
print ()
print ('----------------------------------------------------------------')
print ()

print ('Part 4')
print ('Using the math module.')

'''
Part 4 – Using the math module
1. Add a comment section to your program.
2. Ask the user for four values. The values must be entered as whole numbers
(integers).
3. Print the sum of the values
4. Print the average of the values
5. For each of the four values print the difference between that value and the
average. The individual values and differences could be as displayed below or
put into a table with labels. The difference for each value must be POSITIVE.
'''

print ()
print () 
value1 = int(input('Enter the first whole number value ---> '))
value2 = int(input('Enter the second whole number value --> '))
value3 = int(input('Enter the third whole number value ---> '))
value4 = int(input('Enter the fourth whole number value --> '))
valuesSum = value1 + value2 + value3 + value4
valuesAvg = valuesSum / 4
print ()
print ()
print ('Sum of the values:', valuesSum)
print ('Average of the values:', '{:.2f}'.format(valuesAvg)) ### used format as a way to get 2 decimal places.  But left Average as negative if possible.  
print ('Value 1:', value1, '  Difference', '{:.2f}'.format(abs(value1 - valuesAvg))) ### used abs() to make all Differences positive and format to get 2 decimal places.
print ('Value 2:', value2, '  Difference', '{:.2f}'.format(abs(value2 - valuesAvg)))
print ('Value 3:', value3, '  Difference', '{:.2f}'.format(abs(value3 - valuesAvg)))
print ('Value 4:', value4, '  Difference', '{:.2f}'.format(abs(value4 - valuesAvg)))
print ()
print ('----------------------------------------------------------------')
print ()
