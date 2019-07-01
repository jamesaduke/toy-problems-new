l# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

# Examples:
# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
# tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)

def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'

    # second solution easier to understand way longer though

    def tickets(people):
    change = 'YES'
    twentyfive, fifty, onehundred = 0, 0, 0
    
    for cash in people:
        if change == 'NO':
            break

        if cash == 25:
            twentyfive += 1
        elif cash == 50 and twentyfive > 0:
            twentyfive -= 1
            fifty += 1
        elif cash == 100:
            if fifty > 0 and twentyfive > 0:
                fifty -= 1
                twentyfive -= 1
                onehundred += 1
            elif twentyfive > 2:
                twentyfive -= 3
                onehundred += 1
            else:
                change = 'NO'
        else:
            change = 'NO'
            
    return change