import turtle as t

#Create function to draw the Fibonacci sequence
def drawFibonacci(terms, scale):
    #Specify screensize dimension
    scr = t.Screen()
    scr.setup(width = 1.0, height = 1.0)
    
    #Specify backgorun and pen colors
    t.bgcolor('black')
    t.pencolor('lightgreen')
    t.width(2)

    #Specify speed of drawing; 0 = fastest
    t.speed(0)

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

#Call function to draw
drawFibonacci(14,1)

t.done()