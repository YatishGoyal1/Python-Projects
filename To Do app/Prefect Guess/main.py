import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
   a = int(input("Guess The No.: "))
   if(a>n):
      print("Lower No. pls!")
      guesses+=1
   elif(n>a):
      print("Higher No pls!")
      guesses+=1

print(f"You Have Guessed The no in {guesses+1} attempt")
      