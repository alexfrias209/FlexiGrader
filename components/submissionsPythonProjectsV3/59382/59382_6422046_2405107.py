#imports

import turtle
import random
import time
import sys

#systems

#creating

#Intro

print('Hello! Welcome to my ME021 Project.')
print('This is a game where you control a spaceship and try to collect as much loot as possible.')
print('Use the arrow keys to move the spaceship and collect the loot!')
while True:
    
    to_start = input('Press Enter to proceed: ')

    if to_start == '':
        print('Good Luck')
        break
    else:
        print('''You're ship exploded! You Die!''')
        game_close = input('')
        sys.exit()


#speed of spaceship
g = 0.1


#coords
delay = 0.1
x = random.randint(-300, 300)
y = random.randint(-300, 300)

#colors
rainbow = ['red','black','green']

r = random.choice(rainbow) #use one of the three colors

#score
score = 0
high_score = 0
weight = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("Score: 0 Weight : 0 High Score: 0", align="center", font=("Courier", 18, "normal"))

#penup() disable the tracks the turtle leaves when it is moved
    
#screen
wn = turtle.Screen()
wn.title("Spaceship")
wn.bgcolor("lightblue")
wn.setup(width=720, height=720)
wn.tracer(0)

#spaceship
spaceship = turtle.Turtle()
spaceship.speed(0)
spaceship.color("red")
spaceship.penup()

#

#shop
shop = turtle.Turtle()
shop.shape("triangle")
shop.color("black")
shop.goto(0,0)
shop.penup()

#loot
loot = turtle.Turtle()
loot.shape("circle")
loot.color(r)
loot.penup()
loot.goto(x,y)
loot.penup()

#controls
def up():
    if spaceship.heading() != 270:
        spaceship.setheading(90)

def down():
    if spaceship.heading() != 90:
        spaceship.setheading(270)
    
def left():
    if spaceship.heading() != 0:
        spaceship.setheading(180)

def right():
    if spaceship.heading() != 180:
        spaceship.setheading(0)

wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
#onkey() binds function to a key on your keyboard

# Game Functions
while True:
    #names on top of shop and spaceship
    spaceship.clear()
    spaceship.penup()
    spaceship.forward(g)
    spaceship.write("Player 1", align="center", font=("Arial", 16, "normal"))
    spaceship.penup()
    shop.clear()
    shop.penup()
    shop.write("Shop", align="center", font=("Arial", 16, "normal"))
    shop.penup()
    
    wn.update()

    #decrease speed of if weight increases by 10 still testing. . .
    if weight >= 5:
        spaceship.forward(0.)
    # reset if spaceship touches borders
    if spaceship.xcor()>350 or spaceship.xcor()<-350 or spaceship.ycor()>350 or spaceship.ycor()<-350:
        time.sleep(1)
        i = random.randint(-250, 250)
        o = random.randint(-250, 250)
        spaceship.goto(i,o) #reset spaceship in a random spot
        
        # reset score
        weight = 0
        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} Weight: {} High Score: {}".format(score,weight, high_score), align="center", font=("Courier", 24, "normal")) 
    
    # spaceship collects loot
    if spaceship.distance(loot) < 20:
        # spawn loot in a different place
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        loot.goto(x,y)

        delay -= 0.001

        # increase score
        weight += random.randint(0, 5)

        pen.clear()
        pen.write("Score: {} Weight: {} High Score: {}".format(score,weight, high_score), align="center", font=("Courier", 24, "normal"))
            
        
    if spaceship.distance(shop) < 20:

        score += 1*weight

        weight = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} Weight: {} High Score: {}".format(score,weight, high_score), align="center", font=("Courier", 24, "normal"))
        
        if score > high_score:
            high_score = score #new highscore
        
        pen.clear()
        pen.write("Score: {} Weight: {} High Score: {}".format(score,weight, high_score), align="center", font=("Courier", 24, "normal")) 



