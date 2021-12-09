nap = input()
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def napszam(nap, napok):
    for i in range(7):
        if(nap == napok[i]):
         szam = i+1
         break
    return szam

print(napszam(nap, napok))