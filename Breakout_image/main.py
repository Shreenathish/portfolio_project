import turtle

wn = turtle.Screen()
wn.title("Paddle Movement")
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
ball.shapesize(1.2, 1.2)
ball.color("white")
ball.penup()
ball.speed(0.1)
ball.goto(0, -220)
ball.speed(0.01)
ball_speed_x = 10
ball_speed_y = 10

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

wn.onscreenclick(move_paddle)

def game_loop():

    move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_bounce()

    if ball.xcor() > 290 or ball.xcor() < -290:
        x_bounce()

    if (paddle.ycor() - 10 < ball.ycor() < paddle.ycor() + 10) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        y_bounce()

    check_block_collision()

    wn.update() 
    wn.ontimer(game_loop, 20) 

blocks = []
def create_blocks():
    y = 250
    colors = ['red','yellow','green','blue','purple']
    
    for color in colors:
        for i in range(-250,300,50):
            block = turtle.Turtle()
            block.shape("square")
            block.color(color)
            block.shapesize(stretch_wid=1,stretch_len=2)
            block.penup()
            block.goto(i,y)
            blocks.append(block)
        y = y - 30

def check_block_collision():
    for block in blocks:
        if block.isvisible() and (block.ycor() - 10 < ball.ycor() < block.ycor() + 10) and (block.xcor() - 25 < ball.xcor() < block.xcor() + 25):
            block.hideturtle() 
            y_bounce() 
            blocks.remove(block) 

create_blocks()
game_loop()
wn.mainloop()
