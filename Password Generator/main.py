import random

char = "@#$%^&*_-+=`|:;\"\'<>,./abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

Pass = int(input("Enter The Length Of Your Password: "))

password = ""
for i in range(Pass):
    password+=random.choice(char)
print(password)