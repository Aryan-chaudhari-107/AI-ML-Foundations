# import colorgram
# colors_list = []
#
# colors = colorgram.extract('images.jpg', 30)
#
# for count in colors:
#     r = count.rgb.r
#     g = count.rgb.g
#     b = count.rgb.b
#     new_color = (r,g,b)
#     colors_list.append(new_color)
# print(colors_list)  
''' I used Colorgram as mentioned earlier, but I made a few modifications 
to the code before uploading it to GitHub to prevent other folders and images 
from being included." '''



import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.colormode(255)
tim = t.Turtle()
tim.shape("arrow")
tim.speed(100)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for count in range(1, num_of_dots+1):
    tim.color(random_color())
    tim.dot(20)
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
