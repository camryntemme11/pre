import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor('light pink')

t.speed(0)

t.penup()
t.goto(0,200)
t.pendown()

t.write("All About Me", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(0,-50)
t.pendown()

t.write("Camryn Temme", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(0,-300)
t.pendown()
t.pensize(5)
t.pencolor('purple')

t.fillcolor('purple')
t.begin_fill()
t.circle(90)
t.end_fill()

t.penup()
t.goto(0,0)
t2=turtle.Turtle()
t2.penup()
turtle.addshape("panda.gif")
t2.shape("panda.gif")

t2.goto(100,100)
a = t2.stamp()

t2.penup()
t.goto(0,-50)
turtle.addshape("santa.gif")
t2.shape("santa.gif")

t2.goto(-100,100)
b = t2.stamp()

enter = input("Press enter to go to the next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('light sky blue')

t.penup()
t.goto(0,200)
t.pencolor('black')
t.pendown()

t.write("Favorite Foods", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(-200,100)
t.pendown()
t.pencolor('black')
t.write("Tacos", font=("Arial", 28, "bold"), align="center")

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('black')
t.write("Wings", font=("Arial", 28, "bold"), align="center")

t.penup()
t.goto(200,100)
t.pendown()
t.pencolor('black')
t.write("Pizza", font=("Arial", 28, "bold"), align="center")

t.penup()
t.goto(-100,-250)
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.end_fill()


t.penup()
t.goto(100,200)
t2=turtle.Turtle()
t2.penup()
turtle.addshape("tacos.gif")
t2.shape("tacos.gif")

t2.goto(-100,-25)
a = t2.stamp()

t2.penup()
t.goto(100,200)
turtle.addshape("wings.gif")
t2.shape("wings.gif")

t2.goto(100,-25)
b = t2.stamp()

enter = input("Press enter to go to the next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('dark orchid')

t.penup()
t.goto(0,200)

t.write("Hobbies", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(-230,100)
t.pendown()
t.pencolor('black')
t.write("Softball", font=("Arial", 20, "bold"), align="center")

t.penup()
t.goto(-100,100)
t.pendown()
t.pencolor('black')
t.write("Volleyball", font=("Arial", 20, "bold"), align="center")

t.penup()
t.goto(50,100)
t.pendown()
t.pencolor('black')
t.write("Swimming", font=("Arial", 20, "bold"), align="center")

t.penup()
t.goto(200,100)
t.pendown()
t.pencolor('black')
t.write("Shopping", font=("Arial", 20, "bold"), align="center")

t.pencolor('black')
t.fillcolor('cadet blue')
t.penup()
t.goto(-200,-300)
t.pendown()
t.begin_fill()
t.goto(-100,-150)
t.goto(0,-300)
t.goto(-200,-300)
t.end_fill()

t.penup()
t.goto(100,200)
t2=turtle.Turtle()
t2.penup()
turtle.addshape("softball.gif")
t2.shape("softball.gif")

t2.goto(-100,-25)
a = t2.stamp()

t2.penup()
t.goto(100,200)
turtle.addshape("shopping.gif")
t2.shape("shopping.gif")

t2.goto(100,-25)
b = t2.stamp()

enter = input("Press enter to go to the next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('cadet blue')

t.penup()
t.goto(0,200)
t.pencolor('black')
t.pendown()

t.write("Favorite Movie", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(0,80)
t.pencolor('red')
t.pendown()

t.write("Home Alone", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(-100,-200)
t.pencolor('red')
t.fillcolor('green')
t.pendown()
t.begin_fill()
t.circle(90,180)
t.end_fill()

t.penup()
t.goto(0,200)
t.pencolor('black')
t.pendown()

t.penup()
t.goto(100,200)
t2=turtle.Turtle()
t2.penup()
turtle.addshape("Home alone 1.gif")
t2.shape("Home alone 1.gif")

t2.goto(-100,-25)
a = t2.stamp()

t2.penup()
t.goto(100,200)
turtle.addshape("home alone robbers.gif")
t2.shape("home alone robbers.gif")

t2.goto(100,-25)
b = t2.stamp()

enter = input("Press enter to go to the next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('Light Coral')

t.penup()
t.goto(0,200)
t.pencolor('black')
t.pendown()

t.write("Favorite Sport", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(0,80)
t.pencolor('Light Blue')
t.pendown()

t.write("Softball", font=("Arial", 35, "bold"), align="center")

t.penup()
t.goto(50,-75)
t.pendown()
t.pencolor('light sky blue')
t.fillcolor('khaki')

t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()





t.penup()
t.goto(0,0)
t2=turtle.Turtle()
t2.penup()
turtle.addshape("softballsport.gif")
t2.shape("softballsport.gif")

t2.goto(100,-200)
a = t2.stamp()

t2.penup()
t.goto(0,-50)
turtle.addshape("pitching.gif")
t2.shape("pitching.gif")

t2.goto(-100,-200)
b = t2.stamp()


turtle.done()