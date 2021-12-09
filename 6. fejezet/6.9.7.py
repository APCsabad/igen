ora = int(input())
perc = int(input())
masodperc = int(input())


def masodperc_valtas(ora, perc, masodperc):
    masodpercben = ora * 3600 + perc * 60 + masodperc
    return masodpercben
   

print(masodperc_valtas(ora, perc, masodperc))
   