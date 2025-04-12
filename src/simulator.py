# src/simulator.py

from field import Field
from car import Car

class Simulator: 
    def __init__(self, field_width, field_heights, car_data_list):
        # car_data_list: list of dicts: { 'car': Car, 'commands': 'FFL' }

        # creating the field object with width and height given by user
        self.field = Field(field_width, field_heights)

        # storng and saving all the cars and their commands in a list concder each item as diectrionry
        self.car_data = car_data_list

        # this was added to maybe store car positions later
        self.positions = {}  # keep it just in case, might help with tracking/ debugging


    def run(self):
        # checking for the the longest command length among all cars, added by user
        steps_max = max(len(c['commands']) for c in self.car_data)

        for step in range(steps_max): # loop through every step one by one

            curr_posit = {}  # maybe using later for stroing all next moves

            for data in self.car_data:
                car = data['car']
                commands = data['commands']

                if not car.active or step >= len(commands):  # skip if car is already crash or has no more commands
                    continue  

                command = commands[step]  #get commend for the current step

                if command == 'L':
                    car.rotate_left() # rotate to left function calling

                elif command == 'R':
                    car.rotate_right()  # rotate to left function calling

                elif command == 'F': # get next position
                    next_x, next_y = car.move_forward()

                    # check if mov is valid insde feild
                    if not self.field.is_within_bounds(next_x, next_y):
                        continue  # skipping this move if out of the boundry 

                    # checking if any other car is already at that spot
                    for other in self.car_data:
                        if other == data or not other['car'].active:
                            continue # ignoring by self and dead cars

                        ox, oy, _ = other['car'].get_position()
                        
                        
                        #collision will detected here
                        if next_x == ox and next_y == oy:
                            # print(f"- {car.name}, collides with {other['car'].name} at ({next_x},{next_y}) at step {step + 1}")
                            # print(f"- {other['car'].name}, collides with {car.name} at ({next_x},{next_y}) at step {step + 1}")
                            
                            # build the message from current car’s point of view
                            car1_name = car.name                 # get name of car that is moving
                            car2_name = other['car'].name          # get name of the other car it crashed into
                            collision_x = next_x                  # x coordinates where they both hit
                            collision_y = next_y                  # y coocoordinats where the car both hit
                            collision_step = step + 1               # step number (1-indexed, looks better)

                            # print collision information for car1
                            print(f"- {car1_name}, collides with {car2_name} at ({collision_x},{collision_y}) at step {collision_step}")

                            # print collision information for car2 
                            print(f"- {car2_name}, collides with {car1_name} at ({collision_x},{collision_y}) at step {collision_step}")

                            car.active = False
                            other['car'].active = False
                            break
                    else:
                         # if no collisiion then go ahead and update car position
                        car.update_position(next_x, next_y)

        # Print final positons of cars that exsist
        print("\nAfter simulation, the result is:")
        for data in self.car_data:
            car = data['car']
            if car.active:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
