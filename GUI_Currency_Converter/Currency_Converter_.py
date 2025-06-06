from tkinter import *

class Currency_Converter:
    """ Currency Converter class code for desigining 
    Gui and functions to perform this operations 
    """
    def __init__(self):
        root = Tk()
        root.geometry("400x400")
        root.resizable(width='false',height='false')
        root.title("Currency Converter")
        # Add first Label on main Window
        label_one = Label(root,text="Indian Rupee",font="times 15 bold",fg='GREEN',bg="WHITE")
        label_one.grid(row=1,column=1)
    
        # add Entry widget 
        self.entry = Entry(root,bg="white",relief=SUNKEN,width=35)
        self.entry.grid(row=1,column=2)
        
        # Add second label on main window
        label_two = Label(root,text="Select Country",font="times 15 bold",fg='red',bg="WHITE")
        label_two.grid(row=2,column=1)
        
        # Add first button convert in the main window 
        botton_one = Button(root,text="Convert",font="times 15 bold",fg='black',bg='grey',command=self.currency_convertor)
        botton_one.grid(row=3,column=1)
        
        # Add second button
        button_two = Button(root,text="Clear All",font="times 15 bold",fg='black',bg='grey',command=self.clear)
        button_two.grid(row=4,column=1)
        
        # add text widget 
        self.result = Text(root,height=2,width=30,font="times 10 bold",bg='white')
        self.result.grid(row=3,column=2)
        
        # country_name variable is used to get the value of choice
        # "select country"  e.g. USD
        
        self.country_name = StringVar(root)
        self.country_name.set("Select Country")
        
        # country and currency value equivalent to indian 1 RS
        
        self.options = {
            "USD" : 0.012,
            "Australian Dollar" : 0.018,
            "United Arab Emirates Dirham" : 0.044,
            "Japanese Yen" : 1.82,
            "Russian Ruble": 1.11
        }
        
        # add the option menu to main window 
        self.option_menu = OptionMenu(root,self.country_name,*self.options)
        self.option_menu.grid(row=2,column=2,sticky="ew")
        
        root.mainloop()
    
    def clear(self):
        """ Clear entry, text and unselected selected country
        """
        self.entry.delete(0, END)
        self.result.delete(1.0, END)
        self.country_name.set(None)
    
    
    def currency_convertor(self):
        """ The function helps to take the value entered from entry
            field i.e. ammount in rs 
            and convert it to selected currency 
        """
        try:
            # ammount_rs is stores the indian rupee
            ammount_rs = self.entry.get()
            # selected_country  is stores the selected country name 
            selected_country = self.country_name.get()
            selected_country_currency_value = self.options.get(selected_country,None)
            """ Now, Convert value to float 
            """
            try:
                currency = float(selected_country_currency_value)
                ammount = float(ammount_rs)
                converted_ammount = currency * ammount
                self.result.delete(1.0, END)
                self.result.insert(INSERT,"ammount in ",INSERT,selected_country
                        ,INSERT,"=",INSERT,converted_ammount)
                
            except TypeError as error:
                print("Please Select Target Country or",error)
        except ValueError as error:
            print(error)
            

Currency_Converter()
        