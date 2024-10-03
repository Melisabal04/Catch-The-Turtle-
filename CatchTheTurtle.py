import turtle
import time
import random


scor=0
grid_size=10
turtle_list=[]
game_running=True

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")



def scor_count(x,y):
    global scor
    if game_running:
      scor +=1
      show_scor.clear()
      show_scor.write(f"Scor: {scor}", align="center", font=("Arial", 12, "normal"))

show_scor=turtle.Turtle()
show_scor.penup()
show_scor.hideturtle()
show_scor.goto(0,220)
show_scor.write(f"Scor: {scor}", align="center", font=("Arial", 12, "normal"))


def myTurtle(x,y):
    turtle_instance=turtle.Turtle()
    turtle_instance.shape("turtle")
    turtle_instance.color("green")
    turtle_instance.penup()
    turtle_instance.goto(x* grid_size,y*grid_size)
    turtle_list.append(turtle_instance)
    turtle_instance.onclick(scor_count)

x_coordinates=[-20,-10,0,10,20]
y_cordinates=[20,10,0,-10]

for x in x_coordinates:
    for y in y_cordinates:
        myTurtle(x,y)

def hide_turtle():
    for turtle_instance in turtle_list:
        turtle_instance.hideturtle()

def show_turtle_randomly():
    if game_running:
       hide_turtle()
       random.choice(turtle_list).showturtle()
       turtle_screen.ontimer(show_turtle_randomly,1000)

    


def countdown(time_sec):
    global game_running
    while time_sec > 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        show_count.clear()
        show_count.write(f"Countdown: {timeformat}", align="center", font=("Arial", 12, "normal"))
    
    print("TIME IS UP")
    show_count.clear()
    show_count.write("TIME IS UP", align="center", font=("Arial", 12, "normal"))
    game_running=False
    hide_turtle()  
    




show_count=turtle.Turtle()
show_count.penup()
show_count.hideturtle()
show_count.goto(0,250)
show_count.write(f"Countdown: 00:10 ",align="center", font=("Arial", 12, "normal"))
hide_turtle()
show_turtle_randomly()

countdown(10)





turtle.mainloop()