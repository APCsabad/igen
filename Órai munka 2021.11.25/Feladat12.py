import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Negyzet")


Eszti = turtle.Turtle()
Eszti.left(60)
Eszti.forward(100)
Eszti.left(240)
Eszti.forward(100)
Eszti.left(240)
Eszti.forward(100)

Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)

for i in range(6):
    Eszti.forward(90)
    Eszti.left(300)


for i in range(8):
    Eszti.forward(100)
    Eszti.left(45)


a.mainloop() 