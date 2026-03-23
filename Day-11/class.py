class students:
    
    class_year = 2026
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = students(30, 45)
student2 = students("harish", 45)

print(student1.name)

print(student1.age)

print(student2.name)

print(student2.age)


print(student1.class_year)