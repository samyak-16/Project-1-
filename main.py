# PROJECT 1: SNAKE, WATER, GUN GAME
'''
1 for snake
-1 for  water 
0 for gun 

'''
import random 
computer = random.choice([-1,0,1])
yourchoice = (input("Enter your choice : "))
keyvalue={"s": 1, "w":-1, "g":0}
reverse_key_value={1 : "Snake", -1 :"Water", 0 : "Gun" }
you = keyvalue[yourchoice]

print(f"You choose {reverse_key_value[you]} \n Computer chose {reverse_key_value[computer]}")



if computer == you:
    print ("Draw")

else:

    if(computer==-1 and you == 1):
        print("You win")    
    elif (computer==1 and you==-1):
        print("You loose")
    elif (computer==0 and you==1):
        print("You loose")
    elif (computer==1 and you==0):
        print("You Win")
    elif (computer==-1 and you==0):
        print("You loose")
    elif (computer==-1 and you==0):
        print("You Win")
    elif (computer==0 and you==-1):
        print("You Win")

    else:
     print("Something went wrong : ") 

         # We can replace the ladder by the following logic ..   


    #  if computer - you == -1 or computer - you == 2 :
    #      print("You win ")
    #  else:
    #      print("You loose")   
