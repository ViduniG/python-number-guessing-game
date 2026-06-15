import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("python number guessing game")
print(f"select a number between {lowest_number} and {highest_number}")
while True:
    guess = input("Enter your guess: ")
    if guess.isdigit(): 
        guess = int(guess)
        guesses += 1
        if guess < lowest_number or guess > highest_number:
            print(f"That number is out of range please select something between {lowest_number}and {highest_number}")
        elif guess < answer:
            print("Too low try again")
        elif guess > answer:
            print("Too high try again")
        else:
            print("CORRECT!")
            print(f"Answer was {answer}")
            break
                
    else:
        print("Invalid guess")
        print(f"please select a number between {lowest_number} and {highest_number}")
        
