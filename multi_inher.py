class Grand_father():
    def __init__(self, name):
        self.name = name
    
    def tell_story(self):
        print(f"{self.name} tells a story" )


class Father(Grand_father):
    def work(self):
        print(f"{self.name} is working")

class Child(Father):
    def play(self):
        print(f"{self.name} is playing")

 
child = Child("yahya")
child.tell_story()
child.work()
child.play()

    