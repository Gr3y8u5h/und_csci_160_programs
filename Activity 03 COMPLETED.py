'''# list, access via index x[0]
print("hello")
numbers = [0, 1, 2, 3, 4]
for x in numbers:
    print("the number is", x)
print("goodbye")

# tuple
print("hello")
for x in (2, 7, 1):
    print("the number is", x)
print("goodbye")

# dic, access via key
print("hello")
for x in {1: "one", 2: 'two'}:  # 1 is key 'one' is value. Use key to access.
    print("the number is", x)
print("goodbye")'''

'''# string
for c in "Hi!":
    print(c)

print("hello")
times = 6
for x in range(times):
    print("the number is", x)
print("goodbye")

i = 0
while i < 3:
    # i = i + 1
    print("the number is", i)
print("goodbye")'''

i = 0
sum1 = 0
while i < 5:
    num = int(input('enter num'))
    sum1 = num + sum1
    i = i + 1
print(sum1)
