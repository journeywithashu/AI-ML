class Student:
     def __init__(self):
          print("constructor was called...")

stu1 = Student() 

class Student2:
     def __init__(self, name, cgpa): #paramitrized
          self.name = name
          self.cgpa = cgpa

     def get_cgpa(self):
          return self.cgpa 

stu1 = Student2("Rahul",9.0)
stu2 = Student2("Urvashi",8.5)
stu3 = Student2("Shradha",9.5)

print(f"{stu1.name} has cgpa = {stu1 .get_cgpa()}")
