# psedo random numbers 
import random 
x = random.randint(1,6) # random integer(range)
y = random.random() # random number between 0 and 1

print(x)
print(y)

# rock paper scissors
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

# shuffle cards:
cards = [1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)