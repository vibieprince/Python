import json
file=open("JSON TO PYTHON.py","r")
x=file.read()
finaldata=json.loads(x)
print(finaldata)
for a in finaldata:
    print(a)
    print(a['title'],a['user id'])