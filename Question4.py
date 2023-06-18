# Self is basically used for linked our variables inside the function with its class so that variables should be alligned with classes itself.
#Example - 

class self_demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_details(self):
        return self.name,self.age
    
obj = self_demo("Gourav",22)
print(obj.get_details())