# currently: quit by 'q' doesn't work in rus keyboard layout
# currently: if worker steps on goal - he destroys it 
# TODO: 'r' should restart game
# TODO: in prgr: implement Goal - put O in o
# TODO: map selection on start. can list via reg exp all number.txt files in current folder

from msvcrt import getch
import os

fname = 'maps/03.txt'
worker = 'W'
filler = ' '
box = 'O'
goal = 'o'
wall = '#'
map = []

def init():
    global hi, le, map, x, y, goal_x, goal_y
    with open(fname) as f:
        map_file = [line.strip() for line in f]

    for i, line in enumerate(map_file):
        if worker in line:                  # find worker coords
            x = line.index(worker)
            y = i
#            print 'worker:', x, y
        if goal in line:
            goal_x = line.index(goal)
            goal_y = i
#            print 'goal:', goal_x, goal_y
        map.append(list(line))
    else:
        hi = i                              # set map dimensions
        le = len(map[0])

def redraw_map():
    os.system('cls')
    for line in map:
        for char in line:
            print char,
        print '\n'
        
def move(sh_x, sh_y):
    global x, y, goal_x, goal_y
    if (0 <= x+sh_x < le) and (0 <= y+sh_y <= hi) and map[y+sh_y][x+sh_x] != wall:
        #         in bounds of the map             //          can move
        if map[y+sh_y][x+sh_x] == filler or map[y+sh_y][x+sh_x] == goal:
            map[y+sh_y][x+sh_x] = worker
            map[y][x] = filler 
            x = x+sh_x
            y = y+sh_y
            redraw_map()
        elif (0 <= x+sh_x+sh_x < le) and (0 <= y+sh_y+sh_y <= hi) and map[y+sh_y][x+sh_x] == box and map[y+sh_y+sh_y][x+sh_x+sh_x] != wall and map[y+sh_y+sh_y][x+sh_x+sh_x] != box:
            # //        in bounds of the map                       //         box is near        //                 over the box there are no wall or boxes 
            map[y+sh_y+sh_y][x+sh_x+sh_x] = box
            map[y+sh_y][x+sh_x] = worker
            map[y][x] = filler 
            redraw_map()
            if y+sh_y+sh_y == goal_y and x+sh_x+sh_x == goal_x:
                print 'You win!' 
            x = x+sh_x
            y = y+sh_y

        
def catch_key():
    arrows = {72:'up', 75:'left', 77:'right', 80:'down'}
    while True:
        key = getch()
        o = ord(key)
        if key == 'q':  
            break
        #elif key == 'r':
        #    break
        elif o in arrows:
            if arrows[o] == 'left':
                move(-2,0)
            elif arrows[o] == 'right':
                move(2,0)
            elif arrows[o] == 'up':
                move(0,-1)
            elif arrows[o] == 'down':
                move(0,1)
                
init()                
redraw_map()    
catch_key()
