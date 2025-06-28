class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        a = len(arr1)
        b = len(arr2)
        c = len(arr3)
        i = 0
        j = 0
        k = 0
        ans = []
        while i < a and j < b and k < c:
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i+=1
                j+=1
                k+=1
            else:
                if arr1[i] < arr2[j] and arr2[j] == arr3[k]:
                    i+=1
                elif arr2[j]< arr3[k] and arr3[k] == arr1[i]:
                    j+=1
                elif arr3[k] < arr1[i] and arr1[i] == arr2[j]:
                    k+=1
                elif arr1[i] < arr2[j] and  arr2[j]< arr3[k]:
                    i+=1 
                    j+=1
                elif arr1[i] < arr3[k] and arr3[k] < arr2[j]:
                    i+=1
                    k+=1
                elif arr2[j] < arr3[k] and arr3[k] < arr1[i]:
                    j+=1
                    k+=1
        if len(ans) == 0:
            return -1
        return ans

ques = Solution()
arr1 = [1, 5, 10, 20, 40, 80] 
arr2 = [6, 7, 20, 80, 100] 
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(ques.commonElements(arr1,arr2,arr3))