class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = student("Abebe","12")
student2 = student("Kebe","10")
student3 = student("Belay","13")

print(f"{student1.name} is {student1.age} years old.")
print(f"{student2.name} is {student2.age} years old.")
print(f"{student3.name} is {student3.age} years old.")