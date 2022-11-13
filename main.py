import turtle
from shapely.geometry import Polygon, Point
from math import sqrt, sin, cos, radians

turtle.hideturtle()
s = turtle.getscreen()
turtle.left(90)
turtle.speed(0)
list = []
overlap = input("Do you want the leaves to overlap?(Y or N)")
if overlap == 'Y':
    overlap = True
else:
    overlap = False

# x, y is the bottom left
# turtle should always be pointing up
def draw_square(x, y, tilt, base):
    tilt = tilt % 360
    turtle.up()
    turtle.goto(x, y)
    point1 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.left(tilt)
    turtle.down()
    turtle.forward(base)
    point2 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.right(90)
    turtle.forward(base)
    point3 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.right(90)
    turtle.forward(base)
    point4 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.right(90)
    turtle.forward(base)
    turtle.setheading(90)
    p = Polygon([point1, point2, point3, point4])
    list.append(p)

# x, y is the bottom left
def draw_triangle(x, y, tilt, hyp):
    tilt = tilt % 360
    turtle.up()
    turtle.goto(x, y)
    point1 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.down()
    turtle.left(tilt)
    turtle.right(45)
    turtle.forward(hyp / sqrt(2))
    point2 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    ans = (turtle.xcor(), turtle.ycor())
    turtle.right(90)
    turtle.forward(hyp / sqrt(2))
    point3 = (round(turtle.xcor(), 8), round(turtle.ycor(), 8))
    turtle.setheading(90)
    p = Polygon([point1, point2, point3])
    list.append(p)
    return ans

#checks if this polygon can be created
def checker(x):
    for i in list:
        if i.contains(x[0]) or i.contains(x[1]) or i.contains(x[2]):
            return False
    return True

def get_points(x, y, tilt, base):
    turtle.up()
    turtle.goto(x, y)
    point1 = Point((round(turtle.xcor(), 8), round(turtle.ycor(), 8)))
    turtle.left(tilt)
    turtle.right(45)
    turtle.forward(base / sqrt(2))
    point2 = Point((round(turtle.xcor(), 8), round(turtle.ycor(), 8)))
    turtle.right(90)
    turtle.forward(base / sqrt(2))
    point3 = Point((round(turtle.xcor(), 8), round(turtle.ycor(), 8)))
    turtle.setheading(90)
    return [point1, point2, point3]

def generate():
    # state = (object(square is 0, triangle is 1), x, y, tilt, hyp/base)
    q = []
    q.append((0, -50, -200, 0, 100))
    counter = 0
    while len(q) > 0:
        n = q[0]
        q.remove(n)
        b = n[4]
        t = n[3]
        if n[0] == 0:
            draw_square(n[1], n[2], n[3], n[4])
            q.append((1, n[1] - b * sin(radians(t)), n[2] + b * cos(radians(t)), n[3], n[4]))
            # q.append((1, n[1], n[2], n[3] + 90, n[4]))
            # q.append((1, n[1] + b * cos(radians(t)), n[2] + b * sin(radians(t)), n[3] + 180, n[4]))
            # q.append((1, n[1] + b * sin(radians(t)) + b * cos(radians(t)), n[2] + b * cos(radians(t)) + b * sin(radians(t)), n[3] + 270, n[4]))
        else:
            if overlap or checker(get_points(n[1], n[2], n[3], n[4])):
                top = draw_triangle(n[1], n[2], n[3], n[4])
                q.append((0, n[1], n[2], t + 45, b / sqrt(2)))
                q.append((0, top[0], top[1], t + 315, b / sqrt(2)))
        counter += 1
generate()
turtle.done()
