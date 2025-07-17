import turtle
import Day6_1_Game_Set_Up as setup

def solve():
# ===== Your code starts here =====
# Use setup.forward(), setup.left(), setup.right(), and setup.at_goal()
    while not setup.at_goal():
        setup.forward()
        setup.left()
        for _ in range(2):
            setup.forward()
            setup.right()
        setup.forward()
        setup.left()
# ===== Your code ends here =====
     
    setup.check_result()

solve()
turtle.done()
