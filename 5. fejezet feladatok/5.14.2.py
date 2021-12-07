napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def nap(indulas, ejszakak):
    print(napok[indulas])
    ottalvas = indulas + ejszakak + 1
    akt_nap = indulas
    for i in range(ejszakak):
        if(akt_nap == 7):
            akt_nap = 0
        else:
            akt_nap += 1

    print(napok[akt_nap])

nap(0, 137)
    

