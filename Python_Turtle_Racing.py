import turtle
import time
import random

# Defining width and size of turtle screen
WIDTH, HEIGHT = 500, 500
COLORS = ['black', 'red', 'green', 'orange', 'blue', 'yellow', 'purple', 'pink', 'cyan', 'brown']


def get_number_of_turtle_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers you want (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric...Please try again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number is not within the range of 2-10. Please try again')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

# create list of turtles and place on screen in starting position
def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    # use enumerate to give the index and values of the colors
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # points to right by default so this turns the turtle up
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20) # set position of racer
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    # Setting up turtle screen with its properties (width and height)
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!!')

racers = get_number_of_turtle_racers()
init_turtle()

# shuffle my list of colors and select racers up to the specified number
random.shuffle(COLORS)
colors = COLORS[:racers] # slice of the colors up to the number of racers specified
winner = race(colors)
print("The winner of the race is the turtle with color:", winner)
time.sleep(5)
