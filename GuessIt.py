import random
print("Welcome to a simple guessing game")
print("I'm guessing of a number form 10 to 80, why do you tell me the number I'm guessing")
print("Enter a guess, or 'q' to exit the game")

def difficulty():
    
    choice =input("Pick difficulty, (E=Easy, M=Medium, H=Hard) :")

    match choice:
        case 'E':
            print("playing on Easy mode, guess from 1-8")
            return (1, 8)
        case 'M':
            print("playing on Medium mode, guess from 5-80")
            return (5, 80)
        case 'H':
            print("playing on Hard mode, guess from 1-800")
            return (1, 800)
        case _:
            print("Invalid difficulty, you are now playing in the diffault difficulty of 10-80")
            return (10, 80)

def guessing(min_max):
    min_num, max_num =min_max;
    number = random.randint(min_num,max_num)
    attempts = 0
    
    while True:
        userInput = input("enter your guess :")
        
        if userInput== 'q' :
            print(f"Here is your number of attempets :{attempts}")
            print(f"the correct guess was :{number}")
            break
        
        try :
            x = int(userInput)
        except ValueError:
            print("You must enter 'q' to exit..Thank you")
            continue
        attempts +=1

        if x< number :
            print("Your guess is Low")
            print(" ")
            print(f"Number of attempts is :{attempts}")
        elif x> number :
            print("Your guess is too high")
            print(" ")
            print(f"Number of attempts is :{attempts}")

        else :
            x = True
            print("You guessed right")
            print(" ")
            print(f"Number of attempts is :{attempts}")

difficulty_range =difficulty()
guessing(difficulty_range)