StudentData={'ID1':{'Name':['Luna'],'Class':['VI'],'Subject':['Eng,Math,Sci']},'ID2':{'Name':['Iridesa'],'Class':['IX'],'Subject':['Bio,Math,Urdu']},'ID3':{'Name':['Gul'],'Class':['VII'],'Subject':['Chem,Math,Eng']},'ID4':{'Name':['SilverMist'],'Class':['VII'],'Subject':['Sci,Geo,Eng']}} 
Result={}
for Key,Value in StudentData.items():
    if Value not in Result.values():
        Result["key"]=Value
print(Result)
