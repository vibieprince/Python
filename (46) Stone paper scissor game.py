import random
l=['STONE','PAPER','SCISSOR']

while True:
    ccount=0
    ucount=0
    u=int(input(''' START GAME
                1 YES
                2 NO | EXIT
                '''))
    if u ==1:
        for a in range(1,6):
            i = int(input('''
            1 STONE
            2 PAPER 
            3 SCISSOR
            '''))
            if i==1:
                    v="STONE"
            elif i==2:
                      v="PAPER"
            elif i==3:
                      v="SCISSOR"
            else:
                 print("INVALID OPERATION")
            c=random.choice(l)
            if c==v:
                print("Computer choice : ",c)
                print("Your choice : ",v)
                print("Game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(v=="STONE" and c=="SCISSOR") or (v=="PAPER" and c=="STONE") or (v=="SCISSOR" and c=="PAPER"):
                print("Computer choice : ", c)
                print("Your choice : ", v)
                print("You won 1 point ")
                ucount=ucount+1
            else:
                print("Computer choice : ", c)
                print("Your choice : ", v)
                print("You lost")
                ccount=ccount+1
        print()
        if ucount==ccount:
            print("Game Draws")
            print("Your score ",ucount)
            print("Computer score ",ccount)
        elif ucount>ccount:
            print("You won the game")
            print("Your score ",ucount)
            print("Computer score ",ccount)
        else:
            print("You lost the game")
            print("Your score ",ucount)
            print("Computer score ",ccount)
    else:
        break

