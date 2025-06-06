import random as r
lst = [19,20,21,22,23,24,25,26,27]
print("Original List ", lst)
print('='*50)
print("Shuffled Lists ")
print('='*50)
for i in range(5):
    r.shuffle(lst)
    print(lst)