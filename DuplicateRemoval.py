StudentData={'ID1':{'Name':['Luna'],'Class':['VI'],'Subject':['Eng,Math,Sci']},'ID2':{'Name':['Iridesa'],'Class':['IX'],'Subject':['Bio,Math,Urdu']},'ID3':{'Name':['Gul'],'Class':['VII'],'Subject':['Chem,Math,Eng']},'ID4':{'Name':['SilverMist'],'Class':['VII'],'Subject':['Sci,Geo,Eng']}} 
Result={}
for key,value in StudentData.items():
    if value not in Result.values():
        Result[key]=value
print(Result)
