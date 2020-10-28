import turtle as trtl
from math import sqrt
from time import sleep
debug = True

trtl.hideturtle()
trtl.speed(1)
trtl.setheading(0)
trtl.penup()
trtl.goto(-50,0)
trtl.pendown()
def square( x ):
    side = 0
    if debug == True:
        print("length=",x)
    trtlcolor = input("color of walls? ")
    trtl.fillcolor(trtlcolor)
    trtl.begin_fill()
    while side < 4:
        trtl.forward(x)
        trtl.right(90)
        if debug == True:
            print("side",side)
        side += 1
    trtl.end_fill()
    trtl.left(90)
    triangle()
def triangle():
    trilength= ip*sqrt(2)/2
    side = 0
    if debug == True:
        print("Triangle length =",trilength)
    else:
        pass
    trtlcolor = input("color of roof? ")
    trtl.fillcolor(trtlcolor)
    trtl.begin_fill()
    trtl.right(45)
    trtl.forward(trilength)
    trtl.right(90)
    trtl.forward(trilength)
    trtl.end_fill()
    door()
def door():
    windowsize = ip/4
    trtl.penup()
    trtl.goto(-50,0)
    trtl.setheading(0)
    trtl.forward(ip/5)
    trtl.right(90)
    trtl.forward(ip)
    trtl.setheading(90)
    trtl.pendown()
    trtl.fillcolor("brown")
    trtl.begin_fill()
    trtl.pensize(3)
    trtl.forward(ip/3)
    trtl.right(90)
    trtl.forward(ip/6)
    trtl.right(90)
    trtl.forward(ip/3)
    trtl.end_fill()
    trtl.setheading(90)
    trtl.forward(ip/6)
    trtl.left(90)
    trtl.penup()
    trtl.forward(ip/30)
    trtl.pendown()
    trtl.pensize(1)
    trtl.fillcolor("yellow")
    trtl.begin_fill()
    trtl.circle(ip/75)
    trtl.end_fill()


ip = int(input("how big house "))
if debug == True:
    print("input =",type(ip))
if ip < 200:
    square(ip)
else:
    while ip >= 200:
        print("the number must be smaller than 200!\n")
        sleep(2)
        ip = int(input("how big house \n"))
    square(ip)



ws = trtl.Screen()
ws.mainloop()