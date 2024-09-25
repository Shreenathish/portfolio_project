import turtle

wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=0.8, stretch_len=0.8)
ball.color("white")
ball.penup()
ball.goto(0, -220)

ball_speed_x = 5
ball_speed_y = 5

score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

speed_increments = {
    'red': 1.5,
    'yellow': 1.2,
    'green': 1.0,
    'blue': 0.8,
    'purple': 0.5
}

hit_colors = set()

def move_paddle(x, y):
    if -240 < x < 240:
        paddle.goto(x, -250)
    elif x <= -240:
        paddle.goto(-240, -250)
    else:
        paddle.goto(240, -250)

def move():
    global ball_speed_x, ball_speed_y
    x = ball.xcor() + ball_speed_x
    y = ball.ycor() + ball_speed_y
    ball.goto(x, y)

def y_bounce():
    global ball_speed_y
    ball_speed_y *= -1

def x_bounce():
    global ball_speed_x
    ball_speed_x *= -1

blocks = []
def create_blocks():
    global blocks
    blocks.clear()
    y = 250
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    
    for color in colors:
        for i in range(-250, 300, 50):
            block = turtle.Turtle()
            block.shape("square")
            block.color(color)
            block.shapesize(stretch_wid=1, stretch_len=3)
            block.penup()
            block.goto(i, y)
            blocks.append(block)
        y -= 30

def update_score():
    global score
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def check_block_collision():
    global ball_speed_x, ball_speed_y, score
    for block in blocks:
        if block.isvisible():
            if (block.ycor() - 10 < ball.ycor() < block.ycor() + 10) and (block.xcor() - 30 < ball.xcor() < block.xcor() + 30):
                block.hideturtle()
                blocks.remove(block)
                score += 1
                update_score()

                block_color = block.color()[0]
                if block_color not in hit_colors:
                    hit_colors.add(block_color)
                    ball_speed_x += speed_increments[block_color] * (1 if ball_speed_x > 0 else -1)
                    ball_speed_y += speed_increments[block_color] * (1 if ball_speed_y > 0 else -1)

                y_bounce()
                return

def reset_game():
    global score, ball_speed_x, ball_speed_y, hit_colors
    score = 0
    ball_speed_x = 5
    ball_speed_y = 5
    hit_colors.clear()
    ball.goto(0, -220)
    update_score()
    create_blocks()

def game_loop():
    move()
    if ball.ycor() <= -280:
        reset_game()
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_bounce()
    if ball.xcor() > 290 or ball.xcor() < -290:
        x_bounce()
    if (paddle.ycor() - 10 < ball.ycor() < paddle.ycor() + 10) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        y_bounce()
    
    check_block_collision()

    wn.update()
    wn.ontimer(game_loop, 30)

wn.onscreenclick(move_paddle)

create_blocks()
game_loop()
wn.mainloop()
