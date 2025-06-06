class Recursion:
    first = - 1
    last = - 1
    def findOccurance(self,str , index, element):
        if index == len(str):
            print(f"First Occurence of {element} is {Recursion.first} and Last is {Recursion.last}")
            return
        curr_char = str[index]
        if curr_char == element:
            if Recursion.first == -1:
                Recursion.first = index
            else:
                Recursion.last = index
        self.findOccurance(str, index + 1, element)
            

re = Recursion()
re.findOccurance("asdssbdeqanu", 0, "a")
