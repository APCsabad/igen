a = int(input("Ennyi óra múlva szóljon:"))
nap = 24
jelenleg = int(input("Jelenlegi idő:"))
b = True
szamolas = a + jelenleg

while b:
    if(szamolas > 24):
        szamolas -= 24
    else:
        b = False

print(szamolas)