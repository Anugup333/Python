s = list(map(str,input("Enter the list : ").split()))
L=list(s)
subs = [[],]
subs += [[L[j] for j in range(len(L)) if 1<<j&i] for i in range(1,1<<len(L))]
print(subs)

