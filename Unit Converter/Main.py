def km_to_m(km):
    print(f"{km*1000} Meters")
def m_to_km(m):
    print(f"{m/1000} KM")
def g_to_kg(g):
    print(f"{g/1000} KG")
def kg_to_g(kg):
    print(f"{kg*1000} Grams")
def l_to_ml(l):
    print(f"{l*1000} Mili Liters")
def ml_to_l(ml):
    print(f"{ml/1000} Liters")
print("--Welcome--")
print("1.Kilo Meters To Meters")
print("2.Meters To Kilo Meters")
print("3.Kilo Gram To Gram")
print("4 Gram To Kilo Gram")
print("5.Liters To MiliLiters")
print("6.Mililiters To Liters")
print("7.Exit Program")

while True:
    User = int(input("Choose The No from(1-7):"))
    if User == 1:
       km = int(input("Enter The Value: "))
       km_to_m(km)
    elif User == 2:
       m = float(input("Enter The Value: "))
       m_to_km(m)
       
    elif User == 3:
       kg = int(input("Enter The Value: "))
       kg_to_g(kg)
    elif User == 4:
       g = float(input("Enter The Value: "))
       g_to_kg(g)
    elif User == 5:
      l = int(input("Enter The Value: "))
      l_to_ml(l)
    elif User == 6:
      ml = float(input("Enter The Value: "))
    elif User == 7:
      break
    else:
      print("Please Enter A valid No")
    

