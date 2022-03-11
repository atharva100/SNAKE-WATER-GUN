# PROJECT 1 : SNAKE , WATER , GUN  GAME

import random
from re import A
print("**********SNAKE \U0001F40D WATER \U0001F4A6 GUN \U0001F52B****************")
print("  ")        
print("  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F  \U0001F31F    ")
  
def game():
    
    print("comp Turn : Snake(s) , water(w) or gun(w)?")

    # comp turn using random function

RandNum = random.randint(1,3)           
if RandNum == 1:
    comp ='s'
elif RandNum == 2:
    comp = 'w'
elif RandNum == 3:
    comp = 'g'
  
player = input("player Turn : Snake(s) \U0001F40D  , water(w) \U0001F4A6 or gun(g) \U0001F52B ?    ")

print(" comp chose   " + " " +  str(comp))
print("player chose  " + " " + str(player))   

b = game()    # function call


# rules of game :

if comp==player:    
    print("Its a Tie !  \U0001F643")
elif comp=='s':
    if(player=='w'):
        print("Comp wins!\U0001F4BB \U0001F4BB Better luck next time \U0001F62D  ")
    else:
        print("Congrats,you win! \U0001F601")
elif comp =='w':
    if(player=='s'):
        print("Congrats,you win! \U0001F601")
    else:
        print("Comp wins! \U0001F4BB \U0001F4BB  Better luck next time \U0001F62D")
elif comp =='g':
    if(player=='s'):
        print("Comp wins! \U0001F4BB \U0001F4BB Better luck next time \U0001F62D")
    else:
        print("Congrats, you win ! \U0001F601")


print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")

