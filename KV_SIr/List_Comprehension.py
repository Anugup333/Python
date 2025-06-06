# print("Enter the list of values seperated by space: ")
# lst = [float(val) for val in input().split()]
# print("Content of List ",lst)
# print("Type of List ",type(lst))

# print("Enter List of Values Separated by Comma:")
# posvals=[ float(val)    for val in input().split(",")  if float(val)>0 ]
# print("Possitive Values=",posvals)

# m=3
# n=3
# lst=[(i,j) for i in range(m)  for j in range(n)]
# for x in lst:
#     print(x)
# print(lst)

def findWordLenghth():
    print("Enter the words seperated by spaces: ")
    return {word:len(word) for word in input().split()}

def maxLengthWord(wordLength):
    maxLength = max(wordLength.values())
    word = (word for word,val in wordLength.items() if val==maxLength )
    print("Max Length Word is ",tuple(word))

a = findWordLenghth()
maxLengthWord(a)
