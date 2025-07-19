import turtle
import Day6_2_Game_Set_Up as setup  
import importlib
importlib.reload(setup) 

setup.print_positions()  # Print start and goal positions

setup.setup_game()

def solve_maze():
# ===== Your code starts here =====
# Use setup.front_is_clear(), setup.right_is_clear(), setup.move(),
# setup.turn_left(), setup.turn_right(), and setup.at_goal().
    while setup.front_is_clear():
        setup.move()
    setup.turn_left()

    while not setup.at_goal():
        if setup.right_is_clear():
            setup.turn_right()
            setup.move()
        elif setup.front_is_clear():
            setup.move()
        else: 
            setup.turn_left()
# ===== Your code ends here =====

# Check result after game play
def game_result():
    if setup.at_goal():  # Show success if reached the goal
        setup.show_success_message()
    elif not setup.front_is_clear():  # Show failure if blocked by wall
        setup.show_failure_message()

solve_maze()   # Solve the maze
game_result()  # Display the result
turtle.done()
