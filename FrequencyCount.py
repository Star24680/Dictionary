TestDictionary={'Codingal':2,'Is':2,'Best':2,'For':2,'Coding':1}
print("OriginalDictionary: "+str(TestDictionary))
K=2
Res=0
for key in TestDictionary:
    if TestDictionary[key]==K:
       Res=Res+1
print("Frequency of K is: "+str(Res))