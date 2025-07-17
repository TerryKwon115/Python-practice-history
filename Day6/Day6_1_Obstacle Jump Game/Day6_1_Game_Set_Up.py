import turtle

# Turtle objects
t = turtle.Turtle()
t.hideturtle()
t.color("black")

# Obstacle positions
obstacle_xs = [-67, -7, 53, 113]
obstacles = [(x, 0) for x in obstacle_xs]

# Goal and correct path
goal = (130, 10)
correct_path = [
    (-110, 10), (-80, 10), (-80, 40), (-50, 40), (-50, 10),
    (-20, 10), (-20, 40), (10, 40), (10, 10), (40, 10),
    (40, 40), (70, 40), (70, 10), (100, 10), (100, 40),
    (130, 40), (130, 10)
]
player_path = []

# Player (turtle) setup
player = turtle.Turtle()
player.penup()
player.goto(-110, 10)
player.setheading(0)
player.shape("turtle")
player.color("green")
player.pendown()

# Message turtle
m = turtle.Turtle()
m.hideturtle()

# Draw the ground line
def draw_ground():
    t.penup()
    t.goto(-110, 0)
    t.pensize(5)
    t.pendown()
    t.forward(226)
    t.penup()

# Draw one obstacle
def draw_obstacle(x):
    t.goto(x, 0)
    t.setheading(90)
    t.pendown()
    for _ in range(2):
        t.forward(30)
        t.right(90)
        t.forward(4)
        t.right(90)
    t.penup()

# Draw all obstacles
def draw_obstacles():
    for x in obstacle_xs:
        draw_obstacle(x)

# Movement functions
def forward():
    player.forward(30)
    log_position()

def left():
    player.left(90)

def right():
    player.right(90)

# Record the current position only
def log_position():
    pos = (round(player.xcor()), round(player.ycor()))
    player_path.append(pos)
    
    if pos == goal:
        check_result()

# Check final result only when player reaches the goal
def check_result():
    m.clear()
    if player_path == correct_path:
        m.penup()
        m.goto(0, 80)
        m.color("blue")
        m.write("Success !", align="center", font=("Arial", 20, "bold"))
    else:
        m.penup()
        m.goto(0, 80)
        m.color("red")
        m.write("Fail !", align="center", font=("Arial", 20, "bold"))

# Check if player is at the goal
def at_goal():
    return round(player.xcor()) == goal[0] and round(player.ycor()) == goal[1]

# Check if wall is in front
def wall_in_front():
    heading = player.heading()
    dx = round(30 * turtle.cos(heading * 3.14 / 180))
    dy = round(30 * turtle.sin(heading * 3.14 / 180))
    next_pos = (round(player.xcor() + dx), round(player.ycor() + dy))
    return next_pos in obstacles

# Start the game
draw_ground()
draw_obstacles()
player_path.append((-110, 10))
