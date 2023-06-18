# __init__ function is contructor which is used to pass the Input variable in the classes.
#Example - 

class constructor_demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_details(self):
        return self.name,self.age
    
obj = constructor_demo("Gourav",22)
print(obj.get_details())