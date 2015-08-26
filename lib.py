controls = {
    65: 'up',
    66: 'down',
    68: 'left',
    67: 'right',
    113: 'q',
}

tiles = {
    'off': '\033[0m',         # Text Reset
    'black': '\033[0;100m',   # intense Black
    'blue': '\033[0;104m',    # intense Blue
    'yellow': '\033[0;103m',  # intense Yellow
    'green': '\033[0;102m',   # intense Green
    'white': '\033[0;107m',   # intense White
    'cyan': '\033[0;106m',
}

obj_color = {
    # Bold
    'BBlack': '\033[1;30m',       # Black
    'BRed': '\033[1;31m',         # Red
    'BGreen': '\033[1;32m',       # Green
    'BYellow': '\033[1;33m',      # Yellow
    'BIPurple': '\033[1;95m',
    'BBlue': '\033[1;34m',        # Blue
    'BPurple': '\033[1;35m',      # Purple
    'BCyan': '\033[1;36m',        # Cyan
    'BWhite': '\033[1;37m',       # White
}


class Obj:
    pass

    # empty = ' '
    # worker = 'A'
    # box = 'O'
    # wall = '#'
    # goal = 'x'
    # goal_boxed = 'X'


empty = Obj()
empty.file_view = ' '
empty.terminal_view = '   '
empty.tile = tiles['blue']

worker = Obj()
worker.file_view = 'A'
worker.terminal_view = ' V '  # obj_color['BCyan'] + ' V '
worker.tile = tiles['blue']

wall = Obj()
wall.file_view = '#'
wall.terminal_view = '   '
wall.tile = tiles['black']

box = Obj()
box.file_view = 'O'
box.terminal_view = obj_color['BIPurple'] + '|_|'
box.tile = tiles['yellow']

goal = Obj()
goal.file_view = 'x'
goal.terminal_view = obj_color['BGreen'] + '[x]'
goal.tile = tiles['blue']

goal_boxed = Obj()
goal_boxed.file_view = 'X'
goal_boxed.terminal_view = ' X '
goal_boxed.tile = tiles['green']
