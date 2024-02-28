import turtle
import random
from PIL import Image
import numpy as np

# draw text
def drawtext():
    pen.penup()
    pen.goto(screen.canvheight / 2, -200 + 10)
    pen.write("Done", font=("Arial", 12, "normal"))
    pen.pendown()
    
# load image
def openImage(path):
    image = Image.open(path)
    gray_image = image.convert("L")
    image_array = np.array(gray_image)
    return image_array

def convert_color(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# draw image
image_matrix = openImage(r"1996_24.jpg")
def addDots():
    for i, row in enumerate(image_matrix):
        for j, pixel in enumerate(row):
            if pixel > 1:
                pen.penup()
                pen.goto((i * 2) - screen.canvwidth,(j * 2) - screen.canvheight)
                pen.pendown()
                pen.dot(4,convert_color(pixel, pixel, pixel))
    drawtext()

screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
addDots()
screen.mainloop()
