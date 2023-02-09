#SOLVED after looking at the solution. the initial data must be outside the wile loop. for fucks sake
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = 0,17,31,4
lx = light_x
ly = light_y
tx = initial_tx
ty = initial_ty

# game loop
while True:
    remaining_turns = int(44)
    dirx = ""
    diry = ""
    if tx > lx :
        tx -= 1
        dirx = "W"
    elif tx < lx :
        tx += 1
        dirx = "E"

    if ty > ly :
        ty -= 1
        diry = "N"
    elif ty < ly :
        ty += 1
        diry = "S"

    print(diry + dirx)
