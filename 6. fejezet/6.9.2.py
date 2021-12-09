szam = int(input())
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def napszam(szam):
    return napok[szam]

print(napszam(szam))