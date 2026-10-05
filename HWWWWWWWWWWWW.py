import turtle

t = turtle.Turtle()

# Draw the first right-angled triangle
t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(141)

# Move to the starting point for the mirrored triangle
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the mirrored triangle
t.forward(100)
t.right(90)
t.forward(100)
t.right(135)
t.forward(141)

turtle.done()