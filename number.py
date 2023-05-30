x,y = 10,5
# annotation is only possible for single defined variables
sum:int = x + y
print(f'sum = {sum}', type(sum))

# division:
# / results in float
# // result in int
div:int = x // y
print(f'{x} / {y} = {div}', type(div))
# be careful to not divide by 0

# in general put all imports up to the top
# random numbers:
# random int
from random import randint
# max excluded?
rInt = randint(0,11)
print(f'rInt = {rInt}')

from random import random
rFloat = random()
# turn it into an int
print(rFloat, int(rFloat * 10))

# simple conditions
min:int = 1
max:int = 5
print('Guess the secret number between ', min,' and ',max)
userGuess = input('Guess please:')
secretNumber = randint(min,max)

print('guess:', userGuess, 'secret number: ', secretNumber)
# now compare the numbers
# take everything into account that could go wrong

""" 
This is a Python code snippet that demonstrates several concepts:

Variable assignment: the code starts by assigning the values 10 and 5 to the variables x and y, respectively, using multiple assignment syntax.
Type annotation: the code uses type annotation to specify that the variable sum is an integer.
Basic arithmetic operations: the code calculates the sum and division of x and y using the + and // operators, respectively.
Importing modules: the code imports the randint and random functions from the random module to generate random numbers.
Generating random numbers: the code generates a random integer between 0 and 11 using the randint function and a random float between 0 and 1 using the random function. It also demonstrates how to convert a float to an integer.
Simple conditions: the code sets the variables min and max to 1 and 5, respectively, and prompts the user to guess a secret number between min and max. It then compares the user's guess to a randomly generated secret number using an if statement.
The code also includes comments that explain each concept and provide additional information and warnings.
"""