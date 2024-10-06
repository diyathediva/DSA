import random

number = random.randint(1,20)

guess = -1

while guess != number:
    guess = int(input("enter your guess"))
    if guess > number:
        print('guess is too high')
    elif guess <number:
        print('guess is too low')
print('you have guessed correctly')