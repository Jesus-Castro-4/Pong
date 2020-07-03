import turtle
import winsound

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup (width = 800, height = 600)
window.tracer (0)

marcador_a = 0
marcador_b = 0

# Dibujar elementos del juego

# Paleta A 
paleta_a = turtle.Turtle() 
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("red")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350,0)

# Paleta B
paleta_b = turtle.Turtle() 
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("red")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350,0)
# Bola
bola = turtle.Turtle() 
bola.speed(0)
bola.shape("square")
bola.color("yellow")
bola.penup()
bola.goto(0,0)
# Variable para el movimiento de la bola
bola.dx = 0.3
bola.dy = 0.3

# Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Jugador A: 0 || Jugador B: 0", align="center", font=("Courier", 24, "normal"))

# Definicion de las fuciones de movimiento de las paletas
def paleta_a_up():
    y = paleta_a.ycor()
    y += 20
    paleta_a.sety(y)
    if paleta_a.ycor() >250:
        paleta_a.sety(250)

def paleta_a_down():
    y = paleta_a.ycor()
    y -= 20
    paleta_a.sety(y)
    if paleta_a.ycor() < -250:
        paleta_a.sety(-250)

def paleta_b_up():
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)
    if paleta_b.ycor() >250:
        paleta_b.sety(250)

def paleta_b_down():
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)
    if paleta_b.ycor() < -250:
        paleta_b.sety(-250)

# ligando eventos de teclado
window.listen()
window.onkeypress(paleta_a_up,"w")
window.onkeypress(paleta_a_down,"s")
window.onkeypress(paleta_b_up,"Up")
window.onkeypress(paleta_b_down,"Down")
while True:
    window.update()

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Choque de bordes
    if bola.ycor() > 290:
         bola.sety(290)
         bola.dy *= -1
         winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
 
    if bola.ycor() < -290:
         bola.sety(-290)
         bola.dy *= -1
         winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        marcador_a += 1
        pen.clear()
        pen.write("Jugador A : {} || Jugador B:{}".format(marcador_a, marcador_b),align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        marcador_b += 1
        pen.clear()
        pen.write("Jugador A : {} || Jugador B:{}".format(marcador_a, marcador_b),align="center", font=("Courier", 24, "normal"))

    # Choque de pelota con la paleta B
    if(bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paleta_b.ycor()+45 and bola.ycor() > paleta_b.ycor() - 45):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Choque de pelota con la paleta A
    if(bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paleta_a.ycor()+ 45 and bola.ycor() > paleta_a.ycor() - 45):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
       
git remote add origin https://github.com/Jesus-Castro-4/Pong.git
 git push -u origin master 

 
                