# pseudo code for counting loop

counter = 1
endValue = int(input('Enter end value ')) #10000000
while counter <= endValue:
# while counter >= endValue: #if the intent is to count down
    if counter % 10000 == 0:
        print(counter)
    counter = counter + 1
    # counter = counter - 1 #if the intent is to count down
print('All Done')
