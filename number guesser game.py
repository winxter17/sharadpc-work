i=0
print("Welcome to my game, here you have to guess a given number in maximum of 9 tries.\n")
while(i<10):
    a=int(input("Enter your guess here: "))
    i=i+1
    if a==18:
        print("Congratulations you've won the game.")
        print("No. of guesses used: ",i)
        break

    elif a>18:
        print("Your entered number is greater than the number. Try again")
        print("No. of guesses used: ",i)
        continue
    elif a<18:
        print("Your entered number is smaller than the number. Try again")
        print("No. of guesses used: ",i)
        continue
    


