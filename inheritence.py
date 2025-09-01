class Animal():
    def __init__(self, name):
        self.name = name 


    def speak(self):
        print(f"{self.name} makes a sound ")


class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks")
    


animal = Animal("generic animal")
animal.speak()


dog = Dog("buddy")
dog.speak()