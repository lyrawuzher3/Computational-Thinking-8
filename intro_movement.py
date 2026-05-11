import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("cardinal2",0,-200)
s2 = create_sprite("fish",0,200)

# Section 2: define controls for s1
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+10)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-10)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-10, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+10, y)

def draw():
    s1.pendown()

def stop_drawing():
    s1.penup()

def erase():
    s1.clear()

def red_pen():
    s1.color("red")

def green_pen():
    s1.color("green")

def reset(x,y):
    s1.goto(x,y)

#define controls for s2

def move_up2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y+10)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y-10)
    
def move_left2():
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x-10, y)
    
def move_right2(): 
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x+10, y)

def draw2():
    s2.pendown()

def stop_drawing2():
    s2.penup()

def erase2():
    s2.clear()

def red_pen2():
    s2.color("red")

def green_pen2():
    s2.color("green")

def reset2(x,y):
    s2.goto(x,y)

# # Key Controls for s1
#Press w to move up
window.onkeypress(move_up, "w")
#Press s to move down
window.onkeypress(move_down, "s")
# Press a to move to the left
window.onkeypress(move_left, "a")
#Press d to move to the right
window.onkeypress(move_right, "d")
#Press c to draw
window.onkeypress(draw, "c")
#Press v to stop drawing
window.onkeypress(stop_drawing, "v")
#Press b to erase
window.onkeypress(erase, "b")
#Press n to change color of pen to red
window.onkeypress(red_pen, "n")
#Press m to change color of pen to green
window.onkeypress(green_pen, "m")
#Press on screen to reset 
window.onscreenclick(reset)

# # Key Controls for s2
#Press the up key to move up
window.onkeypress(move_up2, "Up")
#Press the down key to move down
window.onkeypress(move_down2, "Down")
# Press the left key to move to the left
window.onkeypress(move_left2, "Left")
#Press the right key to move to the right
window.onkeypress(move_right2, "Right")
#Press y to draw
window.onkeypress(draw2, "y")
#Press u to stop drawing
window.onkeypress(stop_drawing2, "u")
#Press i to erase
window.onkeypress(erase2, "i")
#Press o to change color of pen to red
window.onkeypress(red_pen2, "o")
#Press p to change color of pen to green
window.onkeypress(green_pen2, "p")
#Press on screen to reset 
window.onscreenclick(reset2)

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

def hide2():
    s2.hideturtle()
def show2():
    s2.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")
window.onkeypress(hide2,"g")
window.onkeyrelease(show2, "g")

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()