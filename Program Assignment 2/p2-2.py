print("Define the amount of numbers: ")
uInput = int(input())
myList = []
average = 0
for item in range(uInput):
    print("Enter a number: ")
    number = int(input())
    myList.append(number)
    average = average + number
    
average = average / uInput
print("The average is: ")
print(average)
