from catch_key import catch_key
from lib import controls
# from lib import tiles
from lib import empty, worker, box, wall, goal, goal_boxed


objects = [empty, worker, box, wall, goal, goal_boxed]
area = []
area_width, area_height = 0, 0
worker_x, worker_y = 0, 0
goal_x, goal_y = 0, 0

filename = 'map.txt'
delimiter = '.'


def read_map(filename):
    global area
    global area_width, area_height
    global worker_x, worker_y
    global goal_x, goal_y

    with open(filename) as f:
        area = [line.strip('\n.').split(delimiter) for line in f]

    for j, line in enumerate(area):
        for i, ch in enumerate(line):
            # if ch == goal.file_view:
            #     goal_x = i
            #     goal_y = j
            #     print goal_x, goal_y
            for obj in objects:
                if ch == obj.file_view:
                    line[i] = obj
                    break

    area_width, area_height = len(area[0]), len(area)


def draw():
    for line in area:
        frmt_str = ''
        for obj in line:
            frmt_str += obj.tile + obj.terminal_view
        print frmt_str


def move(x, y):
    for j, line in enumerate(area):
        for i, obj in enumerate(line):
            if obj == worker:
                wx, wy = i, j
                break
    new_wx, new_wy = wx + x, wy + y

    if not 0 < new_wx < area_width:
        return
    if not 0 < new_wy < area_height:
        return
    if area[new_wy][new_wx] == wall:
        return

    if area[new_wy][new_wx] == box:
        if area[new_wy+y][new_wx+x] == wall:
            return
        if area[new_wy+y][new_wx+x] == box:
            return
        # if area[wy][new_wx+x] == goal:
        #     area[wy][wx] = empty
        #     area[wy][new_wx] = worker
        #     area[wy][new_wx+x] = goal_boxed
        #     return

        area[wy][wx] = empty
        area[new_wy][new_wx] = worker
        area[new_wy+y][new_wx+x] = box
        return

    # if area[wy][new_wx] == goal_boxed:
    #     if area[wy][new_wx+x] == wall:
    #         return
    #     if area[wy][new_wx+x] == box:
    #         return

    #     area[wy][wx] = empty
    #     area[wy][new_wx] = worker
    #     area[wy][new_wx+x] = box
    #     return

    area[wy][wx] = empty
    area[new_wy][new_wx] = worker


def main():
    print("\033c")  # clear screen
    read_map(filename)
    draw()

    while True:
        ch = catch_key()
        o = ord(ch)
        print("\033c")  # Equipotential alternatives: os.system('clear') ## os.system('tput reset')

        if o in controls:
            if controls[o] == 'q':
                print 'quit'
                break
            elif controls[o] == 'left':
                move(-1, 0)
                worker.terminal_view = ' < '
                draw()
            elif controls[o] == 'right':
                move(1, 0)
                worker.terminal_view = ' > '
                draw()
            elif controls[o] == 'up':
                move(0, -1)
                worker.terminal_view = ' ^ '
                draw()
            elif controls[o] == 'down':
                move(0, 1)
                worker.terminal_view = ' V '
                draw()


if __name__ == '__main__':
    main()

# v - now worker changes appearance depending on direction of the last move
# TODO: add at least one goal. Make it not erasable
# TODO: get rid of globals
# TODO: 'r' should restart game
