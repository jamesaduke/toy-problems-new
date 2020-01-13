import random
 
hidden = random.randrange(1, 100)

count = 0
while (count < 5):
  count = count +  1
  guess = int(input("Please enter your guess: "))

  if guess == hidden:
    print ("Hit!")
    break
  else:
    print ("WRONG -1 LIFE")
    