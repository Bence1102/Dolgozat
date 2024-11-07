import random
def paros_szamok():
    paros:int=int(input("Adj meg egy páros számot:"))
    while paros%2!=0:
        paros:int=int(input("Adj meg egy páros számot:"))
        print(paros)
        print("Ez nem páros! Adj meg egy páros számot!")
    return paros

def harommal_oszt():
    lista=[]
    i=0
    while i<13:
        szam:int=int(random.random()*(141)+10)
        lista.append(szam)
        i+=1
    return lista

def oszt_3mal(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]%3==0):
            db+=1
        i+=1  
    return  db


fef
    
