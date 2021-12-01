import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Szabályos Háromszög")


Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.speed(100)


def sokszog_rajzolas(t, n, sz,):
    for i in range(n):
        t.forward(sz)
        t.left(360//n)


def szabalyos_haromszog(t, sz):
    sokszog_rajzolas(t, 3, sz)

szabalyos_haromszog(Eszti, 55)

a.mainloop() 