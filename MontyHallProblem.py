# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:01:10 2020
@author: Ekene Obi
Student Id: 31-03-030-20-2
Email: ekene.obi.2020@student.ism.de
"""

'''
Write a one-round simulation of the Monty Hall Problem (“Let’s make a deal”) according to the following rules:
(6 points)
a) Write a function that randomly defines where the first price (a car), the second price (a money envelope) and the third price (a Zonk) is hidden.
b) Let the player choose one of the doors (e.g. 1,2.3).
c) The moderator will never open the door with the first prize behind it. But once the player has chosen the door with the first price, the moderator will randomly reveal a door with either the second or the third price behind it.
d) After revealing a door, the moderator asks the player whether to change the door or not.
e) Tell the player what price he won.
'''

## Write a function that randomly defines where 
##   the first price (a car), the second price (a money envelope) 
##   and the third price (a Zonk) is hidden.


def checkinput(n):     
    
    import random
    door = ['car', 'money' , 'zonk']   #assign list
    random.shuffle(door)               #shuffle list
    x = door.index('car')              #assign index position 
    y = door.index('money')            #assign index position
    z = door.index('zonk')             #assign index position
    

#   The moderator will never open the door with the first prize behind it. 
#   But once the player has chosen the door with the first price, the 
#   moderator will randomly reveal a door with either the second or the 
#   third price behind it.        
        
    if n == x :
            i=random.choice([y,z])
            if i == y:
                print ("The price in door", y,"is a", door[y])
                #   After revealing a door, the moderator asks the player whether to 
                #   change the door or not.
                print ("would you change your choice door number from ", x ," to door ", z ,"?")
                j = int(input(" input the door number again between these new options above:")) 
                #   Tell the player what price he won.
                if j == x:
                        print ("You have decided to not switch your price in door", x , "is", door[x])
                elif j== z:
                        print ("you have won prize behind door" , z, "which is", door[z])
            else:
                if i == z:
                    print ("The price in door", z,"is a", door[z])
                    #   After revealing a door, the moderator asks the player whether to 
                    #   change the door or not.
                    print ("would you change your choice door number from ", x ," to door ", y, "?")
                j = int(input(" input the door number again between these new options above:")) 
                #   Tell the player what price he won.
                if j == x:
                        print ("You have decided to not switch your price in door", x , "is", door[x])
                elif j== z:
                        print ("you have won prize behind door" , y , "which is", door[y])
    elif n == z :
                print ("The price in door", y , "is a", door[y])
                #   After revealing a door, the moderator asks the player whether to 
                #   change the door or not.
                print ("would you change your choice door number from ", z ," to door ", x, "?")
                j = int(input(" input the door number again between these  new options:")) 
                #   Tell the player what price he won.
                if j == z:
                        print ("You have decided to not switch your price in door", z , "is", door[z])
                elif j== x:
                        print ("you have won prize behind door" , x, "which is", door[x])
    else:
              if n == y :
                print ("The price in door", z , "is a", door[z])
                #   After revealing a door, the moderator asks the player whether to 
                #   change the door or not.
                print ("would you change your choice door number from ", y ," to door ", x)
                j = int(input(" input the door number again between these  new options:")) 
                #   Tell the player what price he won.
                if j == y:
                        print ("You have decided to not switch your price in door", y , "is", door[y])
                elif j== x:
                        print ("you have won prize behind door" , x, "which is", door[x])   
        








def main():
# Let the player choose one of the doors (e.g. 0,1,2).    
    n=int(input("choose the door number, input 0,1, or 2 :"))
    if n <= 2 :
        checkinput(n)
    
    else:
        print ("you have inputed a wrong number")

main()


##############################################################################
##############################################################################
##############################################################################
##############################################################################

'''
Write a program for an arbitrary (e.g. n = 1.000) number of simulations 
for the above problem and count the results of winning the first price.
(5 points)
a) Does it pay off for the participant of the game show to switch doors
    after the moderator has opened one door.
b) Explain the results.
c) What is the expected probability to win if you randomly choose to 
   change doors or not? Backup your expectation by another simulation.
Hint: Compare the relative frequency to win after changing doors with
 the relative frequency to win without changing doors. Write a function
 that determines the wins for a given strategy 
 (“change”, “noChange” or “random”).
'''

import random

def simulations(change, ndoors=3):   
    # Pick a random door out of the ndoors available
    n = random.randint(1, ndoors)
    if change:
       
        revealeddoor = 3 if n==2 else 2
      
        availabledoors = [dnum for dnum in range(1,ndoors+1)
                                if dnum not in (n, revealeddoor)]
        n = random.choice(availabledoors)

    
    return n == 1

def Rsimulations(trials, change, ndoors=3):
    

    nwins = 0
    for i in range(trials):
        if simulations(change, ndoors):
            nwins += 1
    return nwins

ndoors, trials = 3, 90000
nwins_without_switch = Rsimulations(trials, False, ndoors)
nwins_with_switch = Rsimulations(trials, True, ndoors)

print('Probility of wins without changing doors: {:.4f}'
            .format(nwins_without_switch/trials))
print('Probability of wins with changing doors: {:.4f}'
            .format(nwins_with_switch/trials))

'''
Without switching probability of n trials is O.3321
with switching probability of n trails is 0.6684
Because the probability of switching is higher than the probbability of
not switching .
It pays off for the participant to switch when playing the monty hall
game.
note:also attached is a ven diagram
'''

  
