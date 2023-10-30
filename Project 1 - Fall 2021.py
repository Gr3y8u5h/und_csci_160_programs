"""Joshua W George - joshua.w.george@ndus.edu - CSCI-160 Online - Project 1"""

'''
CS160 Computer Science I 
Project 1 
Fall 2021 

This project will calculate some basic information regarding daily sales over a week for a 
business. The program will ask for the total sales for each day in a week. Number the days from 
1 through 7. Once all daily sales when have been entered the program will display some basic 
statistics derived from the information.  

Assignment 
Write a program that asks for the sales for each day of the week. If it matters, think of Sunday 
as being the first day and Saturday the seventh day. Only accept values between $1 and $10000 
for the amount of sales for each day; continue to ask for the sales for a given day until you 
receive an acceptable value. You must use a loop to ask for the daily sales, you cannot code 
individual inputs for each day.  

Once all the daily sales have been entered, display the following information in table format: 
• Total amount of sales for the week. 
• Which day had the highest sales. This can be stated as 1-7, or Sunday through Saturday. 
• The amount from the day with the highest sales. 
• Which day had the lowest sales. This also can be stated as 1-7, or Sunday through Saturday. 
• The amount from the day with the lowest sales. 
• Average sales per day for the week. 
• Given a goal of sales of at least $5000 per day, state how many days met or exceeded the goal.  

Specifics 
• All the daily sales can be entered as integers, we are not worried about pennies when entering the sales. 
• Error checking of inputs is not required other than what is specified in the assignment. 
• Your program must include a comment section with your name, lab day and time, lecture time, and email address. 
• Average sales should have exactly 2 places after the decimal point. 
• No use of lists or any modules to derive the answers. 
• You can assume that there will be one specific day with the highest and lowest amount of sales 
(no “ties” between 2 days). 
'''

#  I'm unsure if I need to define all these variables, but my IDE, pycharm, specifies I should.
day = 1  # started at day 1 to link the first input to Sunday.
dayTotal = 0
goalMet = 0
salesOfDayTotal = 0
salesOfDayHigh = 0  # Set at lowest value so that it'll come up as the program progresses.
salesOfDayLow = 10001  # Set at highest value so that it'll come down as the program progresses.
dayHigh = 0
dayLow = 0
# These two I didn't feel like I needed to declare but my IDE kept telling me I should.
dayDisplayHigh = ''
dayDisplayLow = ''

print()

#  Loop for the 7 day input loop.  Originally I used while True, and the if day <=7, but I wanted to incorporate
#  a for loop.  Also since the loop number was defined at 7 days then I thought it would work better.
for day in range(1, 7 + 1, 1):

    # Used this accumulator for the Average argument.  I couldn't get the day accumulator to work
    # properly, even though it seemed like it would.  WIll need to investigate.
    dayTotal += 1

    # Used to define the days for the first input.  I didn't want to use Day 1, Day 2, Day 3, etc....
    if dayTotal == 1:
        print('Sunday', end=' ', sep='')
    elif dayTotal == 2:
        print('Monday', end=' ', sep='')
    elif dayTotal == 3:
        print('Tuesday', end=' ', sep='')
    elif dayTotal == 4:
        print('Wednesday', end=' ', sep='')
    elif dayTotal == 5:
        print('Thursday', end=' ', sep='')
    elif dayTotal == 6:
        print('Friday', end=' ', sep='')
    elif dayTotal == 7:
        print('Saturday', end=' ', sep='')

    # print('Day ', day, ',', end=' ', sep='')  # iteration one, that I opted to not use.
    salesOfDay = int(input('-Enter sales between $1 and $10000: $'))

    # If someone enters an appropriate number. I didn't account for entry of string variable.
    if 1 <= salesOfDay <= 10000:

        # Initially I tried to combine Highest and Lowest sales and day, but couldn't quite figure it out.
        # So I seperated them.
        # Finding highest sales value.
        if salesOfDayHigh > salesOfDay:
            salesOfDayHigh = salesOfDayHigh
            dayHigh = dayHigh
        else:
            salesOfDayHigh = salesOfDay
            dayHigh = day

        # Finding highest sales day.
        if dayHigh == 1:
            dayDisplayHigh = "Sunday"
        elif dayHigh == 2:
            dayDisplayHigh = "Monday"
        elif dayHigh == 3:
            dayDisplayHigh = "Tuesday"
        elif dayHigh == 4:
            dayDisplayHigh = "Wednesday"
        elif dayHigh == 5:
            dayDisplayHigh = "Thursday"
        elif dayHigh == 6:
            dayDisplayHigh = "Friday"
        elif dayHigh == 7:
            dayDisplayHigh = "Saturday"

        # Finding lowest sales value.
        if salesOfDayLow < salesOfDay:
            salesOfDayLow = salesOfDayLow
            dayLow = dayLow
        else:
            salesOfDayLow = salesOfDay
            dayLow = day

        # Finding lowest sales day.
        if dayLow == 1:
            dayDisplayLow = "Sunday"
        elif dayLow == 2:
            dayDisplayLow = "Monday"
        elif dayLow == 3:
            dayDisplayLow = "Tuesday"
        elif dayLow == 4:
            dayDisplayLow = "Wednesday"
        elif dayLow == 5:
            dayDisplayLow = "Thursday"
        elif dayLow == 6:
            dayDisplayLow = "Friday"
        elif dayLow == 7:
            dayDisplayLow = "Saturday"

        # Finding number of days goal of $5000 was reached.
        if salesOfDay >= 5000:
            goalMet += 1

        # Accumulating the total amount of sales for the week.
        salesOfDayTotal += salesOfDay

        # Stepping to the next day.
        day += 1

    # Else someone enters a number other than expected. I didn't account for entry of string variable.
    else:
        print()
        print('Value must be between $1 and $10000.')
        break

# iteration one print display, that I opted to not use.
# print('Total sales for the week:            $', format(salesOfDayTotal, '8.2f'), sep='')
# print('Day ', dayHigh, ' had the highest sales of:      $', format(salesOfDayHigh, '8.2f'), sep='')
# print('Day ', dayLow, ' had the lowest sales of:       $', format(salesOfDayLow, '8.2f'), sep='')
# print('Avg sales per day for the week:      $', format((salesOfDayTotal / dayTotal), '8.2f'), sep='')
# print('Times the goal of $5000 was reached: ', format(goalMet, '9d'), sep='')
# print('Sunday    = Day 1\n'
#       'Monday    = Day 2\n'
#       'Tuesday   = Day 3\n'
#       'Wednesday = Day 4\n'
#       'Thursday  = Day 5\n'
#       'Friday    = Day 6\n'
#       'Saturday  = Day 7\n')

# I know the table is opposite as normally taught, but I really wanted to print more than just Day 1 and so on,
# So I opted to invert the table so that no matter the day printed the values still stayed in line.  If I ran it
# the other way then when the day string lengths changed the table was affected.
print()
print('${:9.2f}  :Total sales for the week.' .format(salesOfDayTotal))
print('${:9.2f}  :Highest sales, on ' .format(salesOfDayHigh), sep='', end='')
print(dayDisplayHigh, '.', sep='')
print('${:9.2f}  :Lowest sales, on ' .format(salesOfDayLow), sep='', end='')
print(dayDisplayLow, '.', sep='')
print('${:9.2f}  :Avg sales per day for the week.' .format((salesOfDayTotal / dayTotal)))
print('{:10d}  :Times the goal of $5000 was reached.' .format(goalMet))
