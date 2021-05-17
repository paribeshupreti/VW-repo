import turtle



def draw():
    for i in range(12):

        turtle.forward(40)
        turtle.right(80)

    turtle.left(25)
    turtle.backward(150)

    turtle.done()

print(draw())