import random
c=random.randrange(1,101)
n=int(input("Enter your number:- "))
if n==c:
    print(c)
    print("Hurrah! You guessed it right")
elif n>c:
    print(c)
    print("Your guessed number is too high")
elif n<c:
    print(c)
    print("Your guessed number is too low")
else:
    print("Invalid operation")