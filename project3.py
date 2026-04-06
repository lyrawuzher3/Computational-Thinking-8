from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 250
x2 = -300
y2 = 200
x3 = -300
y3 = 150
x4 = -300
y4 = 100


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("flowers")
t1 = create_sprite("flower",x1,y1)
t2 = create_sprite("flower",x2,y2)
t3 = create_sprite("flower",x3,y3)
t4 = create_sprite("flower",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - x3 is the fastest because it increases more than the other sprites and x4 is the slowest because it increases less than the other sprites. The order from fastest to slowest is x3, x1, x2, and then x4.
for i in range(30):
    x1 += 16
    x2 += 8
    x3 += 20
    x4 += 6

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4 
s5 = create_sprite("flower",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Flower 1 wins!")
if x2 >= x1 and x2 >= x3 and x2 > x4:
    s5.write("Flower 2 wins!")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("Flower 3 wins!")
if x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("Flower 3 wins!")


turtle.exitonclick()