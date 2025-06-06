class sorting:
    def __init__(self,arr) -> None:
        self.arr = arr
    
    # Selection sort
    def selection_sort(self):
        n = len(self.arr)
        
        for i in range(n):
            minindex = i
            for j in range(i+1,n):
                if self.arr[j] < self.arr[minindex]:
                    minindex = j
            self.arr[i] , self.arr[minindex] = self.arr[minindex] ,self.arr[i]
        
        print("Sorted array is \n",self.arr)           
    
    # Bubble sort
    def bubble_sort(self):
        n = len(self.arr)
    
        for i in range(n):
            for j in range(n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j] , self.arr[j+1] = self.arr[j+1] ,self.arr[j] 
    
        print("Sorted array is \n",self.arr)  
        
    # Insertion sort
    def insertion_sort(self):
        n = len(self.arr)
        
        for i in range(1,n):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        
        print("Sorted array is \n",self.arr) 
    
if __name__ == "__main__":
    s = sorting([35,72,42,2,0,8,9,21])
    # s.selection_sort()
    # s.bubble_sort()
    s.insertion_sort()
    