s = "Python"
itrobj = iter(s)
while True:
    try:
        print(next(itrobj))
    except StopIteration:
        break

s = (10,"Rossom","Python",102,True)
itrobj = iter(s)
for val in itrobj:
    print(val)

obj = iter(10)
for i in obj:
    print(i)