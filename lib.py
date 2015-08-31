controls = {
    65: 'up',
    107: 'up',  # k
    66: 'down',
    106: 'down',  # j
    68: 'left',
    104: 'left',  # h
    67: 'right',
    108: 'right',  # l
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
empty.color = ''
empty.tile = tiles['blue']

worker = Obj()
worker.file_view = 'A'
worker.terminal_view = ' A '  # obj_color['BCyan'] + ' V '
worker.color = ''
worker.tile = tiles['blue']

wall = Obj()
wall.file_view = '#'
wall.terminal_view = '   '
wall.color = ''
wall.tile = tiles['black']

box = Obj()
box.file_view = 'O'
box.terminal_view = '|_|'
box.color = obj_color['BIPurple']
box.tile = tiles['yellow']

goal = Obj()
goal.file_view = 'x'
goal.terminal_view = ' * '
goal.color = obj_color['BBlack']
goal.tile = tiles['blue']

goal_boxed = Obj()
goal_boxed.file_view = 'X'
goal_boxed.terminal_view = '|_|'
goal_boxed.color = ''
goal_boxed.tile = tiles['green']
