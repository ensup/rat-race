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
    #column == 세로줄, row == 가로줄
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
    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.count_sprouts()

    def count_sprouts(self):
        num = 0
        for l in self.maze:
            num += l.count(SPROUT)
        return num
    
    def is_wall(self, row, col):
        if row < 0 or col < 0:
            return True
        if row >= len(self.maze) or col >= len(self.maze[row]):
            return True
        return self.maze[row][col] == WALL
    
    def move(self, rat, up_down, right_left):
        new_row = rat.row + up_down
        new_col = rat.col + right_left
        if not self.is_wall(new_row, new_col):
            if self.maze[new_row][new_col] == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left -= 1
                self.maze[new_row][new_col] = HALL
            rat.set_location(new_row, new_col)
            return True
        return False

    def get_character(self, row, col):
        if self.is_wall(row,col):
            return WALL
        elif row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        elif row == self.rat_2.row and col == self.rat_2.col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]
    

    def __str__(self):
        row_str_list = []
        for row in self.maze: #Make a sting for each rows
            row_str_list.append(''.join(row))
        maze_str = '\n'.join(row_str_list) # Combine each row into a single maze string
        rat1_str = str(self.rat_1)
        rat2_str = str(self.rat_2)
        result = maze_str + '\n' + rat1_str + '\n' + rat2_str
        return result