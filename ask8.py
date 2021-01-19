import requests
import json 

def get_crypto_equivalent_in_euro(fsym):
    url = f'https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms=EUR' # petaei error an valoume pano apo mia mera diafora, opote pairnoume ena ena ta apotelesmata gia kathe mera
    
    data = requests.get(url).json()
    
    return data['EUR']

f = open("coins.txt", "r")
lines = f.read() 

res = json.loads(lines) 
equiv = get_crypto_equivalent_in_euro(res['fsym']);
euros = equiv*float(res["qty"])

print(f'You have {res["qty"]} coins in {res["fsym"]}, which is {format(euros, ".2f")} euros.') 

# PIGES
# https://www.w3schools.com/python/python_file_open.asp
# https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
# https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python
