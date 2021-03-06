import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)


highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing.
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else: 
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
