import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Negyzet")


Eszti = turtle.Turtle()
Eszti.forward(40)

for i in range(18):
    turtle.forward(45)
    turtle.right(360 / 18)

a.mainloop() 