import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Gyönyörű spirál")


Eszti = turtle.Turtle()
Eszti.shape("turtle")
def spiral():
    for i in range(4):
        Eszti.forward(150)
        Eszti.left(90)


for i in range(21):
    spiral()
    Eszti.left(18)
a.mainloop() 