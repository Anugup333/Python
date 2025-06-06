import json

d1 = {
    'course_name':'Python',
    'fees': 15000,
    'duration':"2 months"
}
# convert in json 
# f = json.dumps(d1)

# print(type(f))
# print(f)

d2 = '{"course_name":"Python","fees": 15000,"duration":"2 months"}'
# json to distinary
x = json.loads(d2)
print(type(x))
print(x)
