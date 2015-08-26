from msvcrt import getch

def catch_key():
    arrows = {72:'up', 75:'left', 77:'right', 80:'down'}
    while True:
        key = getch()
        o = ord(key)
        if key == 'q':  
            break
        elif o in arrows:
            if arrows[o] == 'left':
                move_l()
            elif arrows[o] == 'right':
                move_r()
            elif arrows[o] == 'up':
                move_u()
            elif arrows[o] == 'down':
                move_d()