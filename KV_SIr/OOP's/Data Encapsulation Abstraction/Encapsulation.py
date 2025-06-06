class Account:
    def __init__(self): # Constructor can't be hidden
        self.__acno=123
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4578
        self.bname="SBI"
        
    def dispaccdet(self):
        print("Account Number:",self.__acno)
        print("Account Holder Name:",self.cname)
        print("Account Balance:",self.__bal)
        print("Account PIN:",self.__pin)
        print("Account Branch:",self.bname)