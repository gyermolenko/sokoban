from catch_key import catch_key
from lib import controls
from lib import obj_color
from lib import empty, worker, box, wall, goal, goal_boxed


objects = [empty, worker, box, wall, goal, goal_boxed]
area = []
area_width, area_height = 0, 0
worker_x, worker_y = 0, 0
# goal_x, goal_y = 0, 0
set_of_goals = set()

filename = 'map.txt'
delimiter = '.'


def read_map(filename):
    global area
    global area_width, area_height
    global worker_x, worker_y
    global set_of_goals

    with open(filename) as f:
        area = [line.strip('\r\n.').split(delimiter) for line in f]

    for j, line in enumerate(area):
        for i, ch in enumerate(line):
            if ch == goal.file_view or ch == goal_boxed.file_view:
                set_of_goals.add((i, j))
            for obj in objects:
                if ch == obj.file_view:
                    line[i] = obj
                    break

    area_width, area_height = len(area[0]), len(area)


def draw():
    for line in area:
        frmt_str = ''
        for obj in line:
            frmt_str += obj.tile + obj.color + obj.terminal_view
        print frmt_str


def move(x, y):
    for j, line in enumerate(area):
        for i, obj in enumerate(line):
            if obj == worker:
                wx, wy = i, j
                break
    new_wx, new_wy = wx + x, wy + y

    # if not 0 < new_wx < area_width:
    #     return
    # if not 0 < new_wy < area_height:
    #     return
    if area[new_wy][new_wx] == wall:
        return

    if area[new_wy][new_wx] == box or area[new_wy][new_wx] == goal_boxed:
        if area[new_wy+y][new_wx+x] == wall:
            return
        if area[new_wy+y][new_wx+x] == box:
            return
        if area[new_wy+y][new_wx+x] == goal_boxed:
            return

        if (wx, wy) in set_of_goals:
            area[wy][wx] = goal
        else:
            area[wy][wx] = empty

        if area[new_wy][new_wx] == goal_boxed:
            worker.color = obj_color['BGreen']
            area[new_wy][new_wx] = worker
        else:
            worker.color = obj_color['BWhite']
            area[new_wy][new_wx] = worker

        if area[new_wy+y][new_wx+x] == goal:
            area[new_wy+y][new_wx+x] = goal_boxed
        else:
            area[new_wy+y][new_wx+x] = box
        return

    if area[new_wy][new_wx] == goal:
        worker.color = obj_color['BGreen']
        area[new_wy][new_wx] = worker
        area[wy][wx] = empty
        return

    if (wx, wy) in set_of_goals:
        area[wy][wx] = goal
    else:
        area[wy][wx] = empty
    worker.color = obj_color['BWhite']
    area[new_wy][new_wx] = worker


def i_win():
    for goal_ in set_of_goals:
        if area[goal_[1]][goal_[0]] is not goal_boxed:
            return False

    print 'Congratulations!'
    return True


def main():
    # clear screen. Alternatives: os.system('clear') ## os.system('tput reset')
    print("\033c")
    read_map(filename)
    draw()

    while not i_win():
        ch = catch_key()
        o = ord(ch)
        # print ch, o

        if o in controls:
            if controls[o] == 'q':
                print 'quit'
                break
            elif controls[o] == 'left':
                print("\033c")
                move(-1, 0)
                worker.terminal_view = ' < '
                draw()
            elif controls[o] == 'right':
                print("\033c")
                move(1, 0)
                worker.terminal_view = ' > '
                draw()
            elif controls[o] == 'up':
                print("\033c")
                move(0, -1)
                worker.terminal_view = ' ^ '
                draw()
            elif controls[o] == 'down':
                print("\033c")
                move(0, 1)
                worker.terminal_view = ' V '
                draw()


if __name__ == '__main__':
    main()

# v - now worker changes appearance depending on direction of the last move
# v - added hjkl controls
# v - goal shoud not disapper when stepped over or boxed
# v - make worker green when over the goal
# v - set of goals inst of one goal
# v - add winning game conditions
# v - fixed issue with \r inst of \n
# - choose level
# TODO: get rid of globals
# TODO: 'r' should restart game
