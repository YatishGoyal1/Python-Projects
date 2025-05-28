import requests
import json

city = input("Enter The Name Of the City: ")

url = f"http://api.weatherapi.com/v1/current.json?key=eee055aceddd441aa34145900252705&q={city}%27%20\%20--header%20%27Content-Type:%20application/json"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"] ["temp_c"])