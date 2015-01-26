import turtle

turtle.speed(0)
turtle.delay(0)

def plant(length, n, input):
    turtle.pencolor('#488627')
    length = length * 0.8
    def restore(a, p):
        # moves turtle to p and makes it face a
        turtle.up()
        turtle.setpos(p)
        turtle.setheading(a)
        
        turtle.down()
    # recursion base, defines the variables
    if input == 'f' and n == 0:
        turtle.forward(length)
        return
    elif input == 'x' and n == 0:
        return
    else:
        # Defines the rule for iteration (X F-[[X]+X]+F[+FX]-X), (F  FF)
        """  F means "draw forward", - means "turn left 25°", and + means
        "turn right 25°". X does not correspond to any drawing action and
        is used to control the evolution of the curve. [ corresponds to saving the
        current values for position and angle, which are restored when the corresponding ] is executed."""
        if input == 'x':
            plant(length, n-1, 'f')
            turtle.left(25)
            a1, p1 = turtle.heading(), turtle.pos()
            a2, p2 = turtle.heading(), turtle.pos()
            plant(length, n-1, 'x')
            restore(a2, p2)
            turtle.right(25)
            plant(length, n-1, 'x')
            restore(a1, p1)
            turtle.right(25)
            plant(length, n-1, 'f')
            a3, p3 = turtle.heading(), turtle.pos()
            turtle.right(25)
            plant(length, n-1, 'f')
            plant(length, n-1, 'x')
            restore(a3, p3)
            turtle.left(25)
            plant(length, n-1, 'x')
        if input == 'f':
            plant(length, n-1, 'f')
            plant(length, n-1, 'f')

plant(10, 7, 'x')
