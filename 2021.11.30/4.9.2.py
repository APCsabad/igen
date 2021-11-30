import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Negyzet")


Eszti = turtle.Turtle()
Eszti.shape("turtle")
def negyzet(t, n):
    for i in range(4):
        t.forward(n)
        t.left(90)

n = 20
x = 0
y = 0
for i in range(5):
    negyzet(Eszti, n)
    n += 20
    x += -10
    y += -10
    Eszti.penup()
    Eszti.goto(x, y)
    Eszti.pendown()
a.mainloop() 