def bekeres():    
    b = int(input("Adja meg a könyv oldalszámát:"))
    if(b<150):
        E=True
        return E
    else:
        E=False
        return E
    

while True:
    a = (input("Adja meg a könyv címét:"))
    if(a==""):
        break

    if(bekeres()==True):
        print("A(z) "+a+" Rövid terjedelmü könyv.")
    else:
        print("A(z) "+a+" Hosszú terjedelmü könyv.")


    


        
    
