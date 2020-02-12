'''
import openrouteservice
from openrouteservice.directions import directions
coords = ((17.445231, 78.444912),(17.410336, 78.402744))
client = openrouteservice.Client(key='5b3ce3597851110001cf62488feb2fa344784f60be8f13f1cc007c3c')
routes = directions(client, coords)
l=""
l=routes
n=len(routes)
for i in l:
    print(l)


'''

def get_directions():
   import geopy.geocoders
   from geopy.geocoders import Nominatim
   geolocator = Nominatim()
   address1, (latitude1, longitude1) = geolocator.geocode("ameerpet hyderabad")
   address2, (latitude2, longitude2) = geolocator.geocode("film nagar hyderabad")
   print(address1, latitude1, longitude1)
   print(address2, latitude2, longitude2)
   import requests
   latitude1=17.444425
   longitude1=78.444673
   headers = {
       'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
   }
   call = requests.get('https://route.ls.hereapi.com/routing/7.2/calculateroute.json?apiKey=DsKxYZL6f6V-Ho5msPwEJCZO9ga4l5oKDWohqoP3E28&waypoint0=geo!'+str(latitude1)+','+str(longitude1)+'&waypoint1=geo!'+str(latitude2)+','+str(longitude2)+'&mode=fastest;car;traffic:disabled', headers=headers)
   #print(call.status_code, call.reason)
   #print(call.text)
   ab=""
   ab=call.text
   #print(ab[ab.find("instruction"):])
   import re
   regexPattern = re.compile('instruction')
   iteratorOfMatchObs = regexPattern.finditer(ab)
   indexPositions = []
   count = 0
   for matchObj in iteratorOfMatchObs:
      indexPositions.append(matchObj.start())
      count = count + 1
   #print(count)
   di=[]
   le=[]
   ti=[]
   #print(indexPositions)
   for i in range(0,len(indexPositions)-1):
         step=(ab[indexPositions[i]:indexPositions[i+1]])
         #print(step)
         dire='<span class=\"direction\">'
         leng='<span class=\"length\">'
         time='"travelTime":'
         #d=step.find(dire)
         if "right" in step:
            di.append("right")
         elif "left" in step:
            di.append("left")
         else:
            di.append("continue")
         regexPattern = re.compile('length')
         iteratorOfMatchObs = regexPattern.finditer(step)
         index = []
         count = 0
         for matchObj in iteratorOfMatchObs:
            index.append(matchObj.start())
            count = count + 1
         ghj=step[index[0]+9:index[0]+15]
         if 'km' in ghj:
            r=[]
            r1=ghj.split(" ")
            r.append(1000*float(r1[0]))
            #res = [float(i) for i in ghj.split() if i.isdigit()]
            le.append(r)
         elif 'm' in ghj:
            res = [float(i) for i in ghj.split() if i.isdigit()]
            le.append(res)
         regexPattern = re.compile('travelTime')
         ie=regexPattern.finditer(step)
         index = []
         count = 0
         for matchObj in ie:
            index.append(matchObj.start())
            count = count + 1
         tie=step[index[0]+12:index[0]+16]
         #print(tie)
         r2 = tie.split(",")
         ti.append(int(r2[0]))
         
   return di,le,ti


