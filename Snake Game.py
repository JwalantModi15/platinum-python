import turtle
import random
import time

score = 0
high_score = 0

bodies = []
delay = 0.1
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width = 600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
x = random.randint(-285, 285)
y = random.randint(-285, 285)
food.goto(x,y)

sb = turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.goto(-280,-280)
sb.write(f"Score: 0 | Highest Score: 0", font=("Arial", 12))
sb.ht()

def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+21)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-21)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+21)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-21) 

screen.listen()
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")
screen.onkeypress(moveRight, "Right")
screen.onkeypress(moveLeft, "Left")
while True:
    screen.update()
    if head.distance(food)<=19:
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        food.goto(x,y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("black")
        body.penup()
        bodies.append(body)
        score+=10
        delay-=0.001

        if score>high_score:
            high_score = score
        sb.clear()
        sb.write(f"Score: {score} | Highest Score: {high_score}", font=("Arial", 12))

    for i in range(len(bodies)-1,0,-1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)

    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
     
    move()

    for body in bodies:
        if abs(body.xcor()-head.xcor())<=19 and abs(body.ycor()-head.ycor())<=19:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            score = 0
            delay = 0.1
            for body in bodies:
                body.ht()
            bodies.clear()
            sb.clear()
            sb.write(f"Score: {score} | Highest Score: {high_score}", font=("Arial", 12))

    if head.xcor()>285:
        head.setx(-285)
    if head.xcor()<-285:
        head.setx(285)
    if head.ycor()<-285:
        head.sety(285)
    if head.ycor()>285:
        head.sety(-285)
    
    time.sleep(delay)
    
screen.mainloop()