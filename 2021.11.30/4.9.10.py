def pentagram(ttl):
    

             
    for x in range(5):      
        ttl.forward(100)
        ttl.right(144)
    
                

import turtle

a = turtle.Screen()        
a.bgcolor("lightblue")    

Eszti = turtle.Turtle()      
Eszti.color("HotPink")       

Eszti.penup()                
                            

Eszti.backward(175)          
Eszti.left(90)
Eszti.forward(60)
Eszti.right(90)
Eszti.pendown()

for dummy in range(5):      
    pentagram(Eszti)  
    Eszti.penup()  
    Eszti.forward(350)        
    Eszti.right(144)
    Eszti.pendown()         

a.mainloop()   