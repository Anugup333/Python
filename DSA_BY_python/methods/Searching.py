class searching:
    def __init__(self,array) -> None:
        self.arr = array
    
    # searching Linear search
    def linear_search(self,key):
        n = len(self.arr)
        for i in range(n):
            if self.arr[i] == key:
                print("Element is present at index ",i)
                return
        print("Element is not present ")
    
    def binary_search(self,key):
        # In binary search array is sorted 
        n = len(self.arr)
        l = 0
        r = n - 1
        while l <= r:
            # find mid Index
            mid = l + (r-l)//2
            
            if self.arr[mid] == key:
                print("Element is present at Index ",mid)
                return
            elif self.arr[mid] < key:
                l = mid + 1
            else:
                r = mid - 1
        
        print("Element is not present ")

if __name__ =="__main__":
    lin = searching([12,223,34,576,84])
    lin.linear_search(345)
    bin = searching([12,23,23,33,665,767])
    bin.binary_search(665)
    
    