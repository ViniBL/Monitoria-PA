import turtle

#turtle.shape('turtle')
turtle.hideturtle()
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()

#parede
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()

#reposicao pra janela
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(130)

#janela
turtle.pendown()
turtle.fillcolor('cyan')
turtle.begin_fill()
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()

#reposicao pra porta
turtle.penup()
turtle.right(90)
turtle.forward(130)
turtle.left(90)
turtle.forward(50)
turtle.pendown()

#porta
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

#reposicao pro telhadinho

turtle.penup()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.pendown()

#telhado
turtle.fillcolor('red')
turtle.begin_fill()
turtle.right(30)
turtle.forward(300)
turtle.right(120)
turtle.forward(300)
turtle.end_fill()
