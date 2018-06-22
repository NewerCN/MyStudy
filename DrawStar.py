import turtle as t

t.pensize(5)
t.color("red","red")

t.begin_fill()

t.left(36)
t.fd(200)
for i in range(4):
    t.left(144)
    t.fd(200)

t.end_fill()
t.hideturtle()
t.done()
