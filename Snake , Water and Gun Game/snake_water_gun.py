import random
'''
gun = 0
snake = -1
water = 1
'''
computer = random.randint(0,1)
youstr = input("Enter Your Choice : ")
youdict = { "s":1 , "w":-1 , "g":0}
you = youdict[youstr]
revdict = { 1 : "Snake", -1:"Water" , 0:"Gun"}
print(f"You choose {revdict[you]} \nComputer Choose {revdict[computer]}")
if(computer==you):
    print("it's Draw")
else:
    if(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Win!")