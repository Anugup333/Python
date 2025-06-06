import json
try:
    with open("news.json","r") as fp:
        list_dict_obj = json.load(fp)
        # it return the list and dict obj based on the data in the form of json file
        print("Type of dict_obj = ",type(list_dict_obj))
        print("="*50)
        for record in list_dict_obj:
            for key,val in record.items():
                print(f"\t {key} ---> {val}")
            print()
        print("="*50)
except FileNotFoundError:
    print("File Not Found Error")