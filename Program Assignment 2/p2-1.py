myList = []
average = 0
for item in range(1,101):
    myList.append(item)
    average = item + average

length = len(myList)
average = average / length
print("The average is ")
print(average)
