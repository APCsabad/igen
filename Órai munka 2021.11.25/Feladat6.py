a = 51
nap = 24
jelenleg = 14
b = True
szamolas = a + jelenleg

while b:
    if(szamolas > 24):
        szamolas -= 24
    else:
        b = False

print(szamolas)