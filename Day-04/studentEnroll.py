students = [
    ("Rahul Sharma", "Mathematics"),
    ("Priya Verma", "English"),
    ("Amit Singh", "Science"),
    ("Ajay Singh", "Science"),
    ("Neem Yadav", "Social Studies"),
    ("Neha Yadav", "Social Studies"),
    ("Rohan Gupta", "Computer Science")
]

unique_course = set()

for tup in students:
    unique_course.add(tup[1]) #course

print(unique_course)


for name , course in students:
    if(course == "English"):
        print(name)

#create dictionary

dict = {}

for name, course in students:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
