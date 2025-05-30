import random
import turtle

screen = turtle.Screen()

game_over = False
score = 0
FONT = ('Arial', 30, 'normal')

count_down_turtle = turtle.Turtle()

t = turtle.Turtle()

grid_size = 10
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
top_height = screen.window_height() / 2  # positive height/2 is the top of the screen
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    score_turtle.setposition(0, top_height * 0.9)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)

def make_turtle():
    t.hideturtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)

    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.onclick(handle_click)


def move_turtle():

    if not game_over:
        t.hideturtle()
        t.penup()
        x = random.choice(x_coordinates) * grid_size
        y = random.choice(y_coordinates) * grid_size
        t.goto(x,y )
        t.showturtle()

        screen.ontimer(move_turtle, 700)


def countdown(time):
    global game_over

    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, top_height * 0.8)
    count_down_turtle.clear()

    if time > 0:

        count_down_turtle.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        t.hideturtle()
        count_down_turtle.write("Game Over!", align='center', font=FONT)


def start_game():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    make_turtle()
    move_turtle()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game()
turtle.mainloop()