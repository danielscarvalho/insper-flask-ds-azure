import requests
import random
import string

def ddgquery(query):
    URL = "https://duckduckgo.com/?q="+query+"&format=json&pretty=1"
    response = requests.get(URL)
    ddg = response.json()
    #ddg = requests.get("https://duckduckgo.com/?q="+query+"&format=json&pretty=1").json()
    info = ddg["Abstract"]
    if len(info) > 1:
        return info
    else:
        return "Ops! No data found!" 

def bitcoins():
    URL="https://www.mercadobitcoin.net/api/BTC/trades/"
    response = requests.get(URL)
    return {"btc":response.json()}

def ethereum():
    URL="https://www.mercadobitcoin.net/api/ETH/trades/"
    response = requests.get(URL)
    return {"eth":response.json()}

def weather(latitude, longitude):
    KEY = "ed38d2abac6e6aded3cf1ed68fddb3c6"
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat=' + str(latitude) + '&lon=' + str(longitude) + '&appid='+ KEY
    return requests.get(URL).json()

def newpassword(size=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = characters.replace("'","").replace('"',"").replace("\\","")

    return ''.join(random.choice(characters) for i in range(size))

def geoposition(place):
    URL = "https://nominatim.openstreetmap.org/search?format=json&q=" + place
    response = requests.get(URL).json();
    return response

# Teste	
# print(ddgquery("Madonna"))
# print(ddgquery("Duckduckgo"))
# print(ethereum())
# print(weather(-23.5984834927,-46.6766234833))
# print(newpassword())
# print(newpassword(16))
# print(geoposition("Insper"))
