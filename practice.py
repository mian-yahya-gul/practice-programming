class employ:  
    def __init__(self): #special method/magic method/dender method
        # print ("started executing attributes/data")
        self.id= 123
        self.salary = 50000
        self.designation = "CEO"
        print("attributes initiated")


    def travel(self, destination):
        # print("this tavel method was called manually")
        print(f"employ is now travelling to {destination}")

# creating and object/instance of the class

yahya = employ()

# yahya.travel("peshawar")

# print (yahya.id)
print(type(yahya))