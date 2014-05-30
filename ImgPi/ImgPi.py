import requests
import json



CLIENT_ID = "efed10c55d16860"

#http = urllib3.PoolManager()
#send the client id to the imgur API to get anopnymous access to the site.
header= {"Content-Type": "text", "Authorization": "Client-ID " + CLIENT_ID}
#compile the request along with ID headers
r = requests.get('https://api.imgur.com/3/gallery/r/cyberpunk/top/all/0', headers=header)
#read tje text of the
j = json.loads(r.text)

#print the keys for the dict that is our resonse
for key in j:
    print(key)
#now print what? fuck if i knwo btu it prints the damn image link
count = 0
for image in j[u'data']:
    print(image['link'])
    count += 1

print("total links returned: " + str(count))
#print all keys for key data? iim not even sure what this is im doing? dicts of dicts?
for i in j[u'data'][0]:
    print(i)

print("done with key iteration please continue")
image_list = j[u'data']
print(type(image_list))
print(image_list)
