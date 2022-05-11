#Checking the user has given a valid value

print('Please enter a numerical value: ')
value = int(input())
print(value)

while value < 0 or value > 9:
    print("Invalid")
    print("Enter a value from 0 to 9 : ")
    value = int(input)

print("Value: ", value)
