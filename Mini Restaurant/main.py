Menu ={ "Tea" : 20,"Coffe" : 50, "Burger" : 60 , "Pizza" : 100 , "Sandwich" : 70}

print ("Welcom Sir!")
print("Tea : 20\nCoffe : 50\nBurger : 60 \nPizza : 100 \nSandwich : 70")

Order1 = input("What Do you want to order: ")
Bill = 0
if(Order1 in Menu):
    print(f"The item{Order1} ha been added to your order")
    Bill +=Menu[Order1]
else:
    print(f"This Item is Not available yet")
for order2 in Menu:
  a = input("Dou You wanna order something else!")
  if(a=="yes"):
       order2 = input("What Do you want to order: ")
       print(f"The item {Order1} ha been added to your order")
       Bill +=Menu[order2]
  else:
     print(f"Your Total Bill is Rs{Bill}")
     break
    
