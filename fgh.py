f=open('txt.txt','r')
x=f.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(f.read(), 'html.parser')
contentTable  = soup.find('div', { "class" : "mapbox-directions-step-maneuver"}) # Use dictionary to pass key : value pair
print(contentTable)
for a in soup.findAll('div', attrs={'class':'mapbox-directions-instructions'}):
    name=a.find('div', attrs={'class':'mapbox-directions-step-maneuver'})
    print(name.text)
adf=0
ads=0
import re

ads=(re.findall("<div class=\"mapbox-directions-step-maneuver\">",x))
test_sub="<div class=\"mapbox-directions-step-maneuver\">"
res = [i for i in range(len(x)) if x.startswith(test_sub, i)] 
print(str(res)) 
test_sub="<div class=\"mapbox-directions-step-distance\">"
res1 = [i for i in range(len(x)) if x.startswith(test_sub, i)]
print(str(res1))
di=[]
for i in range(len(res1)):
    if "left" in (x[res[i]+45:res1[i]]):
        di.append("left")
    elif "right" in (x[res[i]+45:res1[i]]):
        di.append("right")
    elif "U-turn" in (x[res[i]+45:res1[i]]):
        di.append("right")
    else:
        di.append("continue")
print(di)
