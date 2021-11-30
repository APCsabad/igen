import turtle       


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Negyzet")


Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.speed(100)
def negyzet(t, n, ):
    for i in range(2):
        t.forward(n)
        t.left(90)

t =10
n =5

for i in range(99):
    negyzet(Eszti, n, )
    n += 5
    
a.mainloop() 