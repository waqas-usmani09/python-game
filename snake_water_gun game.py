'''
1 snake
-1 water
0 gun
'''

print("Enter 1_for_snake : -1_for_water : 0_for_gun")
import random
computer=random.choice([-1,0,1])
you_str=input("enter your choice: ")
youdic={"s":1, "w":-1, "g":0}
reversedic={1:"snake", -1:"water", 0:"gun"}

you = youdic[you_str]

print(f"Your choice {reversedic[you]}\ncomputer choice {reversedic[computer]}")


if (computer==you):
    print("It's draw!!")
else:
    if (computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You win!!")
    elif(computer==-1 and you==1):
        print("You win!!")
    elif(computer==-1 and you==0):
        print("You lose!!")
    elif(computer==0 and you==1):
        print("You lose!!")
    elif(computer==0 and you==-1):
        print("You win!!")
    else:
        print("some thing wrong..")

