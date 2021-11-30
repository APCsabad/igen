import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Negyzet")


Eszti = turtle.Turtle()
def sokszog_rajzolas(t, n, sz,):
    for i in range(n):
        t.forward(sz)
        t.left(360//n)
sokszog_rajzolas(Eszti, 8, 50)

a.mainloop() 