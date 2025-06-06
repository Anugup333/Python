class India:
    def country_type(self):
        print("India is developing Country ")
    
    def lang(self):
        print("Indians can speak multiple Languages") 
        

class USA:
    def country_type(self):
        print("USA is Developed Country ") 
    
    def lang(self):
        print("USA Citizens can speak English Language ") 
    

# main program
i = India()
u = USA()

# This is called Object level Polymorphism

for obj in (i,u):
    obj.country_type()
    obj.lang()