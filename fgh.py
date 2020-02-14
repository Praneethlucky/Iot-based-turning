def remove():
    import os
    os.remove("ChangedFile.csv")
    print("File Removed!")
f=open('txt.txt','r')
x=f.read()
print(x)
import re
ads=(re.findall("<div class=\"mapbox-directions-step-maneuver\">",x))
test_sub="<div class=\"mapbox-directions-step-maneuver\">"
res = [i for i in range(len(x)) if x.startswith(test_sub, i)] 
#print(str(res)) 
test_sub="<div class=\"mapbox-directions-step-distance\">"
res1 = [i for i in range(len(x)) if x.startswith(test_sub, i)]
#print(str(res1))
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
#print(di)
"<div class=\"mapbox-directions-step-distance\">"
test_sub="<div class=\"mapbox-directions-step-distance\">"
res1 = [i for i in range(len(x)) if x.startswith(test_sub, i)]
#print(res1)
le=[]
for i in range(len(res1)):
    step1=x[res1[i]+len(test_sub):res1[i]+len(test_sub)+100]
    step=step1.split("\n")
    i=step[1]
    i=i.split(" ")
    ghj=i[len(i)-1]
    #print(ghj)
    if 'km' in ghj:
        s = ''.join(x for x in ghj if x.isdigit() or x == '.')
        le.append(float(s)*1000)
    else:
        s = ''.join(x for x in ghj if x.isdigit() or x == '.')
        le.append(float(s))  
#print(le)
ti=[]
for i in le:
    if i>20:
        ti.append(int(i/30))
    else:
        ti.append(1)
#print(ti)
for i in range(len(ti)):
    print(di[i],le[i],ti[i])
