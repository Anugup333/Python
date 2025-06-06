def read(n, book, target):
    hash = {}
    for i in range(0,n):
        have = book[i]
        more = target - have
        if more in hash.keys():
            return (hash[more],i)
        hash[have] = i
    return (-1,-1)

arr = [2,7,11,15]
print(read(len(arr),arr,18))