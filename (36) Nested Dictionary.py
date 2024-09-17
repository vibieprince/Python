friends = {'Prince': {'height': '5 inch', 'colour': 'Black'},
        'Krishna': {'height': '3 inch', 'colour': 'Dark black'},
        'Dickup':{'height': 'Not applicable','colour': "Jab hai hee nhi too kyu batau?"}}
print(friends)
friends['Krishna']['height']='8 inch'
print(friends['Prince'])
print()
for k,v in friends.items():
    print(k,v['height'],v['colour'])
