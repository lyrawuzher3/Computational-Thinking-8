from utils import *

#--------------GOAL--------------
# # This game is a cookie clicker but instead of cookies, you get flowers. The goal is to get as much milk jugs as you can. In order to get milk jugs, you have to have 200 flowers.
#--------------CONTROLS--------------
# # Press the space button on the keyboard to get flowers. Press the p button on the keyboard to get milk jugs.

# Section 1 - setup
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # my background
set_background("summer")

# my variables
milk = 0
flowers = 0
flowers_list=[]

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Getting milk
def get_control():
    global milk, flowers


    flowers += 1
    x = random.randint(-300,300)
    y = random.randint(-300,200)
    f1 = create_sprite("flowers",x,y)
    flowers_list.append(f1)


def new_milk():
    global milk, flowers
    if flowers >= 200:
        milk += 1
        flowers-=200
        x = random.randint (-200,200)
        y = random.randint (-200,200)
        create_sprite("milkjug",x,y)
        for i in range(200):
            f1 = flowers_list.pop()
            f1.hideturtle()

# TODO - key and action
window.onkeypress(get_control,"space")
# TODO - 2nd key and action
window.onkeypress(new_milk,"p")




# Section 3 - game loop
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
window.listen()
for i in range(1000000000):
    m1.clear()
    #m1.write(f"hearts:{hearts}\nCost:{cost}\nflowers: {flowers}",font=("Arial",30,"normal") )

    # game loop
    #milk += flowers
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"you have {flowers} flowers \n you have {milk} milk \n you need 200 flowers to get one milk",font = ("Arial", 10, "normal"))

    # end game
    #if hearts == 0:
        #break

    time.sleep(0.01)
    window.update()