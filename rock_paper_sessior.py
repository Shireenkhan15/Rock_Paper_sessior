import random
rock='''
    ______
---'  _____)
     (_____)
     (_____)
     (____)
---,__(___)
'''
paper='''
    _________ 
---'   ______)_
    (__________)_
    (____________)
     (_________)
----.__(______)
'''
scessior='''
   _________ 
---'   _____)
     (__________)
     (___________)
      (______)
----.__(_____)
'''
game_image=[rock,paper,scessior]

user_choice=int(input("what do you choose? type 0 for rock,type 1 for paper and type 2 for sessior \n."))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("computer chose:")
print(game_image[computer_choice])

if user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice ==0 and user_choice ==2:
    print("you lose")
elif user_choice> computer_choice:
    print("you win")        
elif computer_choice > user_choice:
    print("computers wins")
elif computer_choice == user_choice:
    print("it's a draw")
elif user_choice>=3 or user_choice<0:
    print("you type a invalid number you lose")
