class animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass

class Lion(animal):
    def speak(self):
        return f"{self.name} Is a Lion and it ROARs."

class Elephant(animal):
    def speak(self):
        return f"{self.name} is an Elephant and it trumpets"
    
#polimerphism
Zoo =[
    Lion("Simba"),
    Elephant("Dumbo")
]
for animal in Zoo:
    print(animal.speak())