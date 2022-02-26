import random
print('number guessing game')
print('guess number (between 1 and 9):')
number = random.randint(1,9)
canches = 0
while canches <5:
    guess = int(input('enter your guess'))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif guess < number:
        print("your guess was to low")
    elif guess >number:
        print("your guess was to high")
    canches = canches +1
if not canches < 5:
    print('you lose!!! the number is ',number)
