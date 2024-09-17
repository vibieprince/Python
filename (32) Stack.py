l=[]
while True:
    c=int(input('''
        1 Push elements
        2 Pop Elements
        3 Peek elements
        4 Display stack
        5 Exit
        '''))
    if c==1:
        n=input('Enter the value')
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print('Empty stack')
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print('Empty stack')
        else:
            print('Last stack value',l[-1])
    elif c==4:
        if len(l)==0:
            print('Empty stack')
        else:
            print('Display stack',l)
    elif c==5:
        break
    else:
        print('invalid operation')