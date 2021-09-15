import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

#creating the display windowp
win= turtle.Screen()
win.title("Feed the Snake Game")
win.bgcolor("green")
win.setup(width=800, height=800)
win.tracer(0)

#head of the snake

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food in the game

food = turtle.Turtle()
colors= random.choice([ 'red', 'black', 'yellow'])
shapes= random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

#score keeping

pen = turtle.Turtle()
print("pen: ", pen)
print("type: ", type(pen))
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
style=("courier", 28, "bold")
pen.write("Score:0 High Score:0" , align= "center" , font= (style))


def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y= head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x= head.xcor()
        head.setx(x+20)
win.listen()
win.onkeypress(goup, "w")
win.onkeypress(godown, "s")
win.onkeypress(goleft, "a")
win.onkeypress(goright, "d")

#main game
segments=[]
#check for collisions
while True :
    win.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        # hide the segments
        for segment in segments :
            segment.goto(1000,1000)
        #clear the segments list
        segments.clear()
        #reset the score
        score=0
        #reset the delay
        delay= 0.1
        pen.clear()
        pen.write("score:{} high score:{}" .format(score,high_score) ,align="center", font=("courier", 24, "normal") )


        #check for collision with food
    if head.distance(food) < 20:
        x= random.randint(-270,270)
        y= random.randint(-270,270)
        food.goto (x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= .001
        score += 10
        if score > high_score:
            high_score= score
        pen.clear()
        pen.write("Score: {} High Score : {}" .format(score, high_score), align="center", font=("candra", 24, "bold"))
    # unclear..??
    for index in range(len(segments)-1 , 0 , -1):
         x= segments[index-1].xcor
         y= segments[index-1].ycor
         segments[index].goto(x,y)
    if len(segments) > 0:
         x= head.xcor()
         y= head.ycor()
         segments[0].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

             Hide the segments
            for segment in segments:
            segment.goto(1000, 1000)
            # Clear the segments list

           segments.clear()

            #score = 0

            # Reset the delay
            #delay = 0.1

            # Update the score display
    pen.clear()
    wpen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)


win.mainloop()

























