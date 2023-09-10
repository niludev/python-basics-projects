import random

answer = random.randint(1, 99)
name = input('what is your name? ')
guess = input('what is your guess? ')
guess = int(guess)

while guess != answer:
    if guess > answer:
        print('the number is smaller!')
    else:
        print('the number is larger')
    guess = input('what is your guess? ')
    guess = int(guess)

print('wowooooooowwww!!!', name, 'you did it! you rock!')