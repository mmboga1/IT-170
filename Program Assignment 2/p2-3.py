studentName = {"Alice":[80,90,70,100,60], "Bob":[70,75,88,77,82], "Cindy":[60,70,90,80,80], "Don":[66,76,76,69,81], "Ellen":[85,88,78,82,68]}
studentAvg = {"Alice": 0, "Bob": 0, "Cindy": 0, "Don": 0, "Ellen": 0}
number = 0
highest = 0
for item in studentName:
    for i in studentName.get(item):
        number = i + number
    number = number / 5
    studentAvg[item] = number
    if highest < number:
        highest = number
    number = 0
    

print("The highest average is: ")
print(highest)
        


