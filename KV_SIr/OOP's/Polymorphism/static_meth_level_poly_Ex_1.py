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
    
class ShowInfo:
    @staticmethod
    def disp(obj):  # Static Method level Polymorphism
        obj.country_type()
        obj.lang()

# main program
i = India() 
u = USA()

# This is called Static Method level Polymorphism

ShowInfo.disp(i)
ShowInfo.disp(u)