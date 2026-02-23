class Student:
    college_name = "ABC college" #class
    PI = 3.14

    def __init__(self,name,gpa):
     self.name = name #instance
     self.gpa = gpa
     self.PI = 3.14

stu1 = Student("Rahul", 9.2)

print(stu1.PI)