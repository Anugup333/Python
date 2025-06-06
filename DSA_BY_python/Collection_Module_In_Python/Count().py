from collections import Counter

l = ['B','B','C','B','C','A','B','B','A','C']
d = Counter(l)
for i in d:
    print(i," -----> ",d[i])
  
# # with dictionary 
# print(Counter({'A':3, 'B':5, 'C':2}))
  
# # with keyword arguments 
# mp = Counter(A=3, B=5, C=2)

# for it in mp:
#     if mp[it] == 2:
#         print(it)