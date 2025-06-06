import json 
DictData={'ENO': 100, 'ENAME': 'Rossum', 'SAL': 4.5, 'DSG': 'Author'}
print('='*50)
print("Dict Data=",DictData)
print("Type of DictData=",type(DictData))
print('='*50)
with open("data.json",'w') as fp:
    json.dump(DictData,fp)
    print("Dict Object Data Saved in Json File--Verify")
print('='*50)
    