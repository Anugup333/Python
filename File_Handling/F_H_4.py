fp1 = open("F_H_4.txt","w+")
fp1.write("Month1:100\n")
fp1.write("Month2:200\n")
fp1.write("Month3:079\n")
fp1.write("Month4:090\n")
fp1.write("Month5:097\n")
fp1.write("Month6:100\n")
print("The Content of File F_H_4.txt are as Follows:")
fp1.seek(0)
print(fp1.read())
fp1.seek(0)
txt = fp1.readlines()
count = 0
sum = 0
for ch in txt:
    fp1.seek(7+count)
    exp = fp1.readline().strip('\n')
    sum += int(exp)
    count += 12
print("Expenses of last six months: ",sum)
