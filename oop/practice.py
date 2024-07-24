#class 
class dog:
    def __init__(self, name, breed) :
        self.name = name
        self.breed = breed

    def bark(self):
        return "woof"

#object creation
dog1 = dog ("boddy", "golden retriver")
dog2 = dog ("max", "germen shapered")

print(f"{dog1.name} is a {dog1.breed}. He says {dog1.bark()}")