import turtle 

def negyzetrajzolas(toll, hossz): 
    """ Egy h oldalú négyzet rajzolása"""
    for i in range(1):
   
        toll.left(3645)


a = turtle.Screen()
a.bgcolor("lightblue")
a.title("Négyzet rajzolása")


toll = turtle.Turtle()
negyzetrajzolas(toll, 50)


a.mainloop()

