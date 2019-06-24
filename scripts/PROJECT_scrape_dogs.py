import json
import urllib.request
import datetime

date_object = str(datetime.date.today())
print(date_object)


my_PF_key = '####'
my_PF_secret = '####'
#redacted to protect security

biggerarg = 'http://api.petfinder.com/pet.find?key='+my_PF_key+'&animal=dog&location=98106&count=1000&output=full&format=json'
bigdata = json.load(urllib.request.urlopen(biggerarg))
f = open(date_object+'bigdata.json', 'w') 
json.dump(bigdata, f)
f.close()

print(bigdata)
