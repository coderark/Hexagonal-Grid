import collections
import math
import turtle

SIZE = int(input("Size of each hexagon in the grid: "))
COOD = int(input("Grid size: "))
RAD = int(input("Radius of the required circle: "))
CX, CY = map(int,input("Center of Circle: ").split())

chain_code=[]

Point = collections.namedtuple("Point", ["x", "y"])
Hex = collections.namedtuple("Hex", ["q", "r"])

def hex_to_pixel(hex):
    x = SIZE * math.sqrt(3) * (hex.q + hex.r/2)
    y = SIZE * 3/2 * hex.r
    return Point(x, y)

sc=turtle.Screen()
tr=turtle.Turtle()

def init_turtle():
    tr.hideturtle()
    sc.bgcolor("lightgreen")
    sc.title("Hex")
    tr.color("blue")
    tr.pensize(1)
    tr.fillcolor('red')

def draw_hex(hex, fill):
    tr.penup()
    tr.seth(0)
    tr.setpos(hex_to_pixel(hex))
    tr.forward(SIZE)
    tr.left(90)
    tr.pendown()
    if fill:
        tr.begin_fill()
    for i in range(6):
        tr.forward(SIZE);
        tr.left(60)
    if fill:
        tr.end_fill()

def draw_hexgrid():
    sc.tracer(0, 0)
    for i in range(-COOD, COOD):
            for j in range(-COOD, COOD):
                        draw_hex(Hex(i, j), False)
    tr.fillcolor('black')
    for i in range(-COOD, COOD):
        draw_hex(Hex(i, 0), True)
    for j in range(-COOD, COOD):
        draw_hex(Hex(0, j), True)
    sc.update()
    sc.tracer(4,20)

def draw_sym(x, y):
    draw_hex(Hex(CX+x, CY+y), True)
    draw_hex(Hex(CX+y, CY+x), True)
    draw_hex(Hex(CX+x+y, CY-x), True)
    draw_hex(Hex(CX+x+y, CY-y), True)
    draw_hex(Hex(CX+y, CY-x-y), True)
    draw_hex(Hex(CX+x, CY-x-y), True)
    draw_hex(Hex(CX-x, CY-y), True)
    draw_hex(Hex(CX-y, CY-x), True)
    draw_hex(Hex(CX-x-y, CY+x), True)
    draw_hex(Hex(CX-x-y, CY+y), True)
    draw_hex(Hex(CX-y, CY+x+y), True)
    draw_hex(Hex(CX-x, CY+x+y), True)

def draw_circle(r):
    x, y=0, r
    d=0.25
    while x<y:
        draw_sym(x, y)
        x+=1
        if d<0:
            d+=2*x+y+2.5
            chain_code.append(0)
        else:
            y-=1
            d+=(x-y)+2.75
            chain_code.append(1)
    draw_sym(x, y)

def draw_diameter():
    tr.fillcolor('yellow')
    for j in range(1, RAD):
        draw_hex(Hex(CX+0, CY+j), True)
        draw_hex(Hex(CX+0, CY-j), True)

init_turtle()
draw_hexgrid()
tr.fillcolor('red')
draw_hex(Hex(CX, CY), True)
draw_circle(RAD)
draw_diameter()
print("Chain Code: ")
print(chain_code)
sc.mainloop()
