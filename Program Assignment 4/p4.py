import random

stuNameList = ['Alice', 'Bob', 'Cindy', 'David', 'Ellen', 'Frank', 'Grace', 'Hellen']
initialClasses = [110, 315, 316, 121, 223, 328, 136, 336, 140, 243, 346, 150, 253, 356]

class Person:
    def __init__(self, name):
     self.name = name
    def getName(self):
        return self.name
    
class Student(Person):
    def __init__(self, name):
        self.finishedCourseList = []
        self.selectedCourseList = []

    def selectFinishedCourses(self):
        i=0
        while(i<3):
            self.finishedCourseList.append(random.choice(initialClasses))
            i = i+1

        while(len(self.finishedCourseList) != 3):
            choice = random.choice(initialClasses)
            if choice not in self.finishedCourseList:
                self.finishedCourseList.append(choice)
    
    def getSelectedCourseList(self):
        return self.selectedCourseList

    def getFinishedCourseList(self):
        return self.finishedCourseList
        
    def selectCourse(self):
        firstClasses = [110, 315, 316, 121, 223, 328, 136, 336, 140, 243, 346, 150, 253, 356]
        for item in self.finishedCourseList:
            if item == 110:
                firstClasses.append(213)
            if item == 316:
                firstClasses.append(412)
            if item == 223:
                firstClasses.append(326)
            if item == 328:
                firstClasses.append(422)
            if item == 136:
                firstClasses.append(238)
            if item == 243:
                firstClasses.append(345)
            if item == 253:
                firstClasses.append(355)
            if item == 356:
                firstClasses.append(452)

        while(len(self.selectedCourseList) != 3):
            choice = random.choice(firstClasses)
            if choice not in self.selectedCourseList:
                self.selectedCourseList.append(choice)
        
            

for item in stuNameList:
    student = Student(item)
    student.selectFinishedCourses()
    student.selectCourse()
    print("Name: "  + item)
    print("Taken Classes: ")
    print(student.getFinishedCourseList())
    print("Chosen Classes: ")
    print(student.getSelectedCourseList())


    
    
    
                                        

            
                

            

            
        

    





    

