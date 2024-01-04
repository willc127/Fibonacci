import turtle as t
from PIL import Image, ImageGrab

# Create function to draw the Fibonacci sequence
def drawFibonacci(terms, scale):
    # Specify screensize dimension
    scr = t.Screen()
    scr.setup(width=1.0, height=1.0)

    # Specify background and pen colors
    t.bgcolor("black")
    t.pencolor("lightgreen")
    t.width(2)

    # Specify speed of drawing; 0 = fastest
    t.speed(15)

    # Save the turtle animation as a sequence of .gif frames
    frames = []

    # Define initial values of Fibonacci's sequence
    previous = 0
    start = 1

    # Calculate Fibonacci's sequence
    for i in range(0, terms - 1):
        fib = previous + start
        for n in range(
            0, 6
        ):  # Draw a square and ends in initial position of next square
            t.forward(fib * scale)
            t.left(90)
            # Capture the current frame and append it to the frames list
            frame = ImageGrab.grab()
            frames.append(frame)
        t.right(90)
        previous = start  # update previous value
        start = fib
        # Capture the current frame and append it to the frames list
        frame = ImageGrab.grab()
        frames.append(frame)

    # Stop drawing and go to origin
    t.penup()
    t.home()

    # Start next drawing (Spiral)
    t.pendown()
    previous = 0
    start = 1

    for i in range(0, terms - 1):
        fib = previous + start
        t.circle(fib * scale, 90)  # Draw a quarter of a circle
        previous = start
        start = fib
        # Capture the current frame and append it to the frames list
        frame = ImageGrab.grab()
        frames.append(frame)

    # Save the frames as a .gif file
    frames[0].save(
        "turtle_animation.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=2,
        loop=0,
    )
    print(len(frames))

# Call function to draw
drawFibonacci(14, 1)

t.done()
