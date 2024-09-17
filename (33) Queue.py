l=[]
while True:
    n=int(input('''
            1 Push Elements
            2 Pop first element
            3 Front element
            4 Last element
            5 Display stack
            6 Exit'''))
    if n==1:
        p=input("Enter the value :- ")
        l.append(p)
        print(l)
    elif n==2:
        if len(l)==0:
            print("Empty queue")
        else:
            del(l[0])
            print(l)
    elif n==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Front element :- ",l[0])
    elif n == 4:
        if len(l)==0:
            print('Empty Queue')
        else:
            print("Last queue element :- ",l[-1])
    elif n==5:
        if len(l)==0:
            print("Empty queue")
        else:
            print('Stack :- ',l)
    elif n==6:
        break
    else:
        print('ivalid operation')