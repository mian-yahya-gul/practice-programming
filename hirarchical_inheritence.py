class parent():
    def __init__(self,name):
        self.name = name
    

    def greet(self):
        print(f"hello my name is {self.name}")


    #derived class 1
class Child_1(parent):
    
    def play(self):
        print(f"{self.name} is playing")
    
class Child_2(parent):
    def study(self):
        print(f"{self.name} is studying")


child1 = Child_1("yahya")
child2 = Child_2("abdullah")

child1.greet()  #hello my name is yahya
child1.play()   #yahya is studing 

child2.greet()  #hello my name is abdullah
child2.study()  #abdullah is studying

