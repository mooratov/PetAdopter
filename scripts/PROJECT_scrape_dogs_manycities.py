import json
import urllib.request
import datetime

date_object = str(datetime.date.today())
print(date_object)


my_PF_key = '####'
my_PF_secret = '####'
#redacted to protect security


#obtained by sampling geographically distinct top-populated metropolitan areas. One zip code per region (typically, the most populated one of that region)
zips = ['10002', '90011', '60629', '75217', '77084', '20011', '33186', '19120', '31139', '02128'] \
 + ['85032', '94112', '92503', '48228', '98115', '55423', '92154', '33647', '80219', '21215']  \
 + ['63129', '28269', '32828', '97229', '15237', '95823', '89110', '45238', '64118', '78250']

for thezip in zips:

	biggerarg = 'http://api.petfinder.com/pet.find?key='+my_PF_key+'&animal=dog&location='+thezip+'&count=1000&output=full&format=json'
	bigdata = json.load(urllib.request.urlopen(biggerarg))
	f = open(date_object+'bigdata_forzip'+thezip+'.json', 'w') 
	json.dump(bigdata, f)
	f.close()

