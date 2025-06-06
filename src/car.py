# car.py

class Car:

    # storing the Directinos in clockwise order for the rotations
    DIRECTIONS = ['N', 'E', 'S', 'W']

    # storing the moves in Mapping for forward movement in each direction
    MOVES = {
        'N': (0, 1),     # move up
        'E': (1, 0),    # move right
        'S': (0, -1),    # move down
        'W': (-1, 0)    # move left
    }

    def __init__(self, Carname, x, y, direction):
        self.Carname = Carname              # Car's name (unique)
        self.x = x                    # starting x position
        self.y = y                    #  starting y position
        self.direction = direction    # N/S/E/W that on which  way car facing toward
        self.active = True             # use to make the car as hit/dead if it is crashes
    

# ****************************** Rotation Toward Left ***************************


    def rotate_left(self):
        """ Turning the car left (90 degrees). Finds which direction the car is facing right now, moving one step back in the direction list 
If it going before the first one, it jumps to the last oneUpdates the car  direction after turnning"""
        curr_index = Car.DIRECTIONS.index(self.direction)

        new_indx = curr_index - 1

        if new_indx < 0:
            new_indx = 3  # manually loop to the last item to iterate

        # update the car the direction
        self.direction = Car.DIRECTIONS[new_indx]

# ****************************** Rotation Toward Rgiht ***************************

    def rotate_right(self):

        curr_index = Car.DIRECTIONS.index(self.direction)

        # move 1 step to the right (clockwise)
        new_indx = curr_index + 1

        if new_indx >= 4:
            new_indx = 0

        self.direction = Car.DIRECTIONS[new_indx]

# ****************************** Rotation Toward Forward ***************************

    def move_forward(self):

        current_dir = self.direction

        move_values = Car.MOVES[current_dir]  # like (0, 1) if facing North
        
        # how much x and y should change
        direction_y = move_values[1]  
        direction_x = move_values[0]  

        # calculate new x and y if car goes forward
        new_x = self.x + direction_x
        new_y = self.y + direction_y

        return new_x, new_y



# ****************************** Upating the Current Position ***************************

    def update_position(self, new_x, new_y):
        # updating car is current x and y to the new onece direction
        self.x = new_x
        self.y = new_y

    def get_position(self):
        
        return self.x, self.y, self.direction # give back to full current state of the car 

    def __repr__(self):
        return f"{self.Carname} at ({self.x}, {self.y}) facing {self.direction}" 
        # for printing car info easily like: A at (3, 4) facing N showing as mentioned in the requirements
