# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'

class Rat:
    """ A rat caught in a maze. """
    # Write your Rat methods here.
    #column == 세로, row == 가로
    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.col = col
        self.row = row
        self.num_sprouts_eaten = 0
        
    def eat_sprout(self):
        self.num_sprouts_eaten += 1

    def __str__(self):
        return str(self.symbol)+" at ("+str(self.col)+", "+str(self.row)+") ate "+str(self.num_sprouts_eaten)+" sprouts."
    
    def set_location(self, row, col):
        self.row = row
        self.col = col


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

r=Rat(RAT_1_CHAR, 4,3)
r.eat_sprout()
print(r)