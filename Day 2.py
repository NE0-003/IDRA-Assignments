import random

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

number = random.randint(start, end)
attempts = 5

print("Guess the number!")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        attempts -= 1
        if attempts > 0:
            print("Too low! Try again.")
            print("Attempts left:", attempts)
    else:
        attempts -= 1
        if attempts > 0:
            print("Too high! Try again.")
            print("Attempts left:", attempts)

if guess != number:
    print("Game Over! You have used all your attempts.")
    print("The correct number was", number)