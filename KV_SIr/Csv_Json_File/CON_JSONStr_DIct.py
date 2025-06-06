import json
jsonstrdata=' {"ENO":"100","ENAME":"Rossum","SAL":"4.5","DSG":"Author"}'
print("Json Str Data = ",jsonstrdata)
print("Type of Jsonstrdata = ",type(jsonstrdata))
print("="*50)
dict_data = json.loads(jsonstrdata)
print("Dict Data = ",dict_data)
print("Type of dict_data = ",type(dict_data))
print('='*50)
for key,val in dict_data.items():
    print(f"\t {key} ---> {val}")
print("="*50)