# Import des modules nécessaires
import turtle
import time   
import random  
delay = 0.1 
# Mise en place de l'écran
window = turtle.Screen() 
window.title("Snake Game") 
window.bgcolor("black")    
window.setup(width=600, height=600)  
window.tracer(0)
# Tête du serpent
head = turtle.Turtle() 
head.speed(0) 
head.shape("square") 
head.color("white")  
head.penup() 
head.goto(0, 0) 
head.direction = "stop" 
# Nourriture
food = turtle.Turtle() 
food.speed(0) 
food.shape("circle")  
food.color("green")
food.penup() 
food.goto(0, 100)
# Fonctions de déplacement du serpent
def go_up():
    if head.direction != "Down":
        head.direction = "Up"
def go_down():
    if head.direction != "Up":
        head.direction = "Down"
def go_left():
    if head.direction != "Right":
        head.direction = "Left"
def go_right():
    if head.direction != "Left":
        head.direction = "Right"
# Liaison des touches du clavier aux fonctions de déplacement
window.listen()
window.onkey(go_up, "Up")  
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
# Fonction pour déplacer le serpent
def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)
segments = []
# Boucle principale du jeu
while True:
    window.update()  # Met à jour l'écran
    # Vérification des collisions avec les bords de l'écran
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Right"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
    # Vérification de la collision avec la nourriture
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        # Ajout d'un segment au serpent
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
    # Déplacement des segments du serpent
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    # Vérification des collisions avec le corps du serpent
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Right"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
    time.sleep(delay)
