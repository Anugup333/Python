# n = int(input("Enter the number of terms: "))
# arr = []
# for i in range(0,n):
#     arr.append(int(input("Element : ")))

# hash

def checkSameFrequency(s: str) -> bool:
    # write your code here
    map = {}
    for i in s:
        if i not in map:
            map[i] = 0
        map[i] +=1
    
    map2  = {}
    for value in map.values():
        if value not in map2:
            map2[value] = 0
        map2[value] +=1
    
    ans = []

    for value in map2.keys():
        ans.append(value)
    
    if len(ans) > 2:
        return False
    elif (len(ans) == 2 and not(map2[ans[0]] == 1 or map2[ans[1]] == 1)) or (len(ans)==2 and abs(ans[0] - ans[1])>1):
        return False
    return True
