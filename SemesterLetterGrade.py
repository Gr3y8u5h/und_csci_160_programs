percent = float (input('Enter your class percentage '))


if percent >= 70:
   if percent >= 90:
      grade = 'A'
   elif percent >= 80: ### if percent >= 80 and percent < 90:
      grade = 'B'
   elif percent >= 70: ### if percent >= 70 and percent < 80:
      grade = 'C'
   passedClass = True
else:
   if percent >= 60: ### if percent >= 60 and percent < 70:  ### will always run 3, 6, 9, 12, and 15 with the if statement as such.
      grade = 'D'
   else: ### if percent < 60: ### if using an else the way it's setup will always end with F.
      grade = 'F'
   passedClass = False

print ('Letter grade ', grade)
if passedClass:
   print ('Passed Pass/Fail')
else:
   print ('Failed Pass/Fail')
