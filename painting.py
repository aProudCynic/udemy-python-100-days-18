import turtle
import random

colours = [
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209)
]

screen = turtle.Screen()
screen.colormode(255)
cursor = turtle.Turtle()
cursor.speed(10)
for row in range(10):
    for column in range(10):
        cursor.pendown()
        color = random.choice(colours)
        cursor.dot(20, color)
        cursor.penup()
        cursor.forward(50)
    if row % 2 == 0:
        cursor.left(90)
        cursor.forward(40)
        cursor.left(90)
        cursor.forward(50)
    else:
        cursor.right(90)
        cursor.forward(40)
        cursor.right(90)
        cursor.forward(50)
cursor.exitonclick()
