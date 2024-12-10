import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.bgcolor("lightblue")
t = turtle.Turtle()
t3 = turtle.Turtle()
t3.hideturtle()
t.speed(100)

t.penup()
t.goto(0, -250)
t.write("Press Enter to move to the next page", align="center", font=("Arial", 14, "italic"))




t3.penup()
t.penup()
t.goto(-100,-100)
t.pendown()
t.pencolor('red')
t.fillcolor('green')
t.begin_fill()
t.circle(35)
t.end_fill()
t.penup()
t.goto(100,-100)
t.pendown()
t.pencolor('red')
t.fillcolor('green')
t.begin_fill()
t.circle(35)
t.end_fill()



t.penup()
t.goto(0, 75)
t.pendown()
t.write("Turtle Presentation", font=('lora', 30, 'bold'), align="center")
t.penup()
t.goto(0, 50)
t.pendown()
t.write(" By Prasant", font=('arial', 20, 'bold'), align="center")
t.penup()


turtle.addshape("ronaldo.gif")
t.penup()
t3.shape("ronaldo.gif")
a = t3.stamp()
t3.goto(0,0)


enter = input("Press Enter to Continue: ")
t.clear()
t3.clearstamps()
t3.clear()
t.write("Favorite Foods", font=('lora', 30, 'bold'), align="center")
t.penup()
t.goto(0,35)

t.write( "Momo and Chatpate are my favorites!", font=('lora', 20, 'bold'), align="center")
t.goto(100,-100)
t.pencolor('white')
t.fillcolor('blue')
t.begin_fill()
t.end_fill()

t.pendown()
t.fillcolor("white")
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.penup()
t.goto(-150,-100)
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()
t.penup()

screen.bgcolor("lightgreen")
t.clearstamps()
turtle.addshape("momo.gif")
t3.goto(-275,200)
t3.shape("momo.gif")
a = t3.stamp()
t3.goto(-200,0)
turtle.addshape("chapate.gif")
t3.goto(275,200)
t3.shape("chapate.gif")
a = t3.stamp()
t3.goto(200,0)

t.goto(0,-275)
t.penup()
t.write("Press Enter to move to the next page", align="center", font=("Arial", 14, "italic"))

enter = input("Press Enter to Continue: ")
t.clear()
t3.clearstamps()
t.penup()
t.goto(0,75)
t.write("Favorite Movie", font=('lora', 30, 'bold'), align="center")
t.penup()
t.goto(0,35)
t.write("My favorite Movie is K.G.F  ", font=('lora', 20, 'bold'), align="center")
screen.bgcolor("lightpink")
t.begin_fill()
t.end_fill()

t.clearstamps()
turtle.addshape("kgf.gif")
t3.goto(-200,150)
t3.shape("kgf.gif")
a = t3.stamp()

t.penup()
t.goto(-125,-50)
t.pendown()
t.fillcolor("white")
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)

t.penup()
t.goto(100,-50)
t.pendown()
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)


t.end_fill()
t.penup()
t.goto(0,-275)
t.write("Press Enter to move to the next page", align="center", font=("Arial", 14, "italic"))

enter = input("Press Enter to Continue: ")
t.clear()
t3.clearstamps()
t.penup()
t.goto(0,75)
t.pencolor('red')
t.write("Favorite Hobbies", font=('lora', 30, 'bold'), align="center")
screen.bgcolor("lightyellow")
t.fillcolor('red')
t.begin_fill()
t.end_fill()


t3.goto(200,150)
t.penup()
t.goto(-200,-100)
t.pendown()
t.goto(-150,-200)
t.goto(-100,-100)

t.goto(-200,-100)


t.penup()
t.goto(200,-100)
t.pendown()
t.goto(150,-200)
t.goto(100,-100)

t.goto(200,-100)

t.clearstamps()
turtle.addshape("soccer.gif")
t3.goto(-200,150)
t3.shape("soccer.gif")
f = t3.stamp()
t3.goto(-200,150)


t.clearstamps()
turtle.addshape("bad.gif")
t3.goto(-200,0)
t3.shape("bad.gif")
z = t3.stamp()
t3.goto(-200,0)

t.clearstamps()
turtle.addshape("vb.gif")
t3.goto(200,0)
t3.shape("vb.gif")
x = t3.stamp()
t3.goto(200,0)


t.clearstamps()
turtle.addshape("tt.gif")
t3.goto(200,150)
t3.shape("tt.gif")
p = t3.stamp()


t.penup()
t.goto(0,-275)
t.write("Press Enter to move to the next page", align="center", font=("Arial", 14, "italic"))


enter = input("Press Enter to Continue: ")
t.clear()
t3.clearstamps()
t.penup()
t.goto(0,75)
t.write("Favorite Sport", font=('lora', 30, 'bold'), align="center")
screen.bgcolor("Black")



t.penup()
t.goto(-200,-100)
t.pendown()
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)


t.penup()
t.goto(200,-100)
t.pendown()
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)
t.forward(25)
t.left(45)








t.clearstamps()
turtle.addshape("messi1.gif")
t3.goto(-50,150)
t3.shape("messi1.gif")
u = t3.stamp()
t3.goto(-50,150)

t.penup()
t.goto(0,-275)
t.write("Press Enter to move to the next page", align="center", font=("Arial", 14, "italic"))


enter = input("Press Enter to Continue: ")
t.clear()
t3.clear()

t.penup()
t.goto(0,0)
t.pendown()

t.write("The End", font=('lora', 40, 'bold'), align="center")
screen.bgcolor("lightgreen")








turtle.done()