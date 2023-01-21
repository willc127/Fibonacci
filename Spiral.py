import turtle as t
import tkinter as _

#Specify pencolor and screensize dimension
t.screensize(canvwidth=700, canvheight=500, bg="black")
t.pencolor('lightgreen')
t.width(2)

#Specify speed of drawing; 0 = fastest
t.speed(0)

#Define terms of Fibonacci's sequence
terms = 10

#Specify scale for drawing
scale = 5

#Define initial values of Fibonacci's sequence
previous = 0
start = 1

#Calculate Fibonacci's sequence
for i in range(0, terms-1):
    fib = previous + start
    for n in range(0,6): #Draw a square and ends in initial position of next square
        t.forward(fib*scale) 
        t.left(90)
    t.right(90)
    previous = start #update previous value
    start = fib

#Stop drawing and go to origin
t.penup()
t.home()

#Start next drawing (Spiral)
t.pendown()
previous = 0
start = 1

for i in range(0, terms-1):
    fib = previous + start
    t.circle(fib*scale,90) #Draw a quarter of circle
    previous = start
    start = fib

t.done()