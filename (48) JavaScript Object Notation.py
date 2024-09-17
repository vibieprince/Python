import json
d={
    'course name':'python',
    'fees': 15000
}
f=json.dumps(d)
print(f,type(f))