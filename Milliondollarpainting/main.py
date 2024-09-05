import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
color_list = [(218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152), (162, 104, 151)]
t = turtle_module.Turtle()

t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_counts % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()