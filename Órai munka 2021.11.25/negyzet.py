import turtle 

def negyzetrajzolas(toll, hossz): #lehet rövidíteni like: t = toll
    """ Egy h oldalú négyzet rajzolása"""
    for i in range(4):
        toll.forward(hossz)
        toll.left(90)

#---Egy ablak létrehozása és néhány tulajdonság beállítása---
a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Négyzet rajzolása")

#---Négyzet rajzolás és rajz eszköz megadás---
toll = turtle.Turtle()
negyzetrajzolas(toll, 50)

# Ablak bezárása
a.mainloop()

