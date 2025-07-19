import turtle
import random
import time

# Maze configuration
cell_size = 40
start_x = -220
start_y = 140

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Fixed goal position (only maze[2][11] is valid goal)
goal_pos = (11, 2)

# Find valid open cells excluding goal_pos
open_cells = [(x, y) for y in range(len(maze)) for x in range(len(maze[y]))
              if maze[y][x] == 0 and (x, y) != goal_pos]
start_pos = random.choice(open_cells)

# Wall drawer
wall_drawer = turtle.Turtle()
wall_drawer.shape("square")
wall_drawer.color("Black")
wall_drawer.penup()
wall_drawer.hideturtle()

# Goal marker (drawn once only)
goal_marker = turtle.Turtle()
goal_marker.shape("circle")
goal_marker.color("Yellow")
goal_marker.penup()
goal_marker.hideturtle()

# Player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("Green")
player.penup()
player.hideturtle()
player.speed(1)

# Internal state
pos = list(start_pos)
heading = random.choice([0, 90, 180, 270])

def draw_maze():
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            if val == 1:
                wall_drawer.goto(start_x + x * cell_size, start_y - y * cell_size)
                wall_drawer.stamp()

def move():
    global pos, heading
    dx, dy = direction_delta(heading)
    new_x, new_y = pos[0] + dx, pos[1] + dy
    if can_move_to(new_x, new_y):
        pos = [new_x, new_y]
        player.goto(start_x + new_x * cell_size, start_y - new_y * cell_size)
        time.sleep(0.3)
        
def turn_left():
    global heading
    heading = (heading + 90) % 360
    player.setheading(heading)
    time.sleep(0.3)
    
def turn_right():
    global heading
    heading = (heading - 90) % 360
    player.setheading(heading)
    time.sleep(0.3)

def direction_delta(deg):
    return {
        0: (1, 0),
        90: (0, -1),
        180: (-1, 0),
        270: (0, 1),
    }[deg]

def can_move_to(x, y):
    return 0 <= y < len(maze) and 0 <= x < len(maze[y]) and maze[y][x] == 0

def front_is_clear():
    dx, dy = direction_delta(heading)
    return can_move_to(pos[0] + dx, pos[1] + dy)

def right_is_clear():
    dx, dy = direction_delta((heading - 90) % 360)
    return can_move_to(pos[0] + dx, pos[1] + dy)

def at_goal():
    return tuple(pos) == goal_pos

def setup_game():
    turtle.tracer(1)
    draw_maze()
    goal_marker.goto(start_x + goal_pos[0] * cell_size, start_y - goal_pos[1] * cell_size)
    goal_marker.stamp()
    player.setheading(heading)
    player.goto(start_x + pos[0] * cell_size, start_y - pos[1] * cell_size)
    player.showturtle()

def print_positions():
    print("Start Position:", pos)
    print("Goal Position:", goal_pos)

def show_success_message():
    player.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-10, 180)
    turtle.color("blue")
    turtle.write("Maze Escape Successful !", align="center", font=("Arial", 24, "bold"))

def show_failure_message():
    player.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 180)
    turtle.color("red")
    turtle.write("Maze Escape Failed !", align="center", font=("Arial", 24, "bold"))

__all__ = [
    "setup_game", "move", "turn_left", "turn_right",
    "front_is_clear", "right_is_clear", "at_goal",
    "pos", "goal_pos", "print_positions",
    "show_success_message", "show_failure_message"
] 
