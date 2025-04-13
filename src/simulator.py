# src/simulator.py

from field import Field
from car import Car

""" This class handle the simulation logic for all the cars.
initilizing the field with the width and height given by end user, Storing the car objects, and 
Runs a step-by-step simulation of each car's movement, Detects and prints collision information
Outputs final position of all active car which arr not coliided yet """

class Simulator: 
    def __init__(self, field_width, field_heights, car_data_list):
        # car_data_list: list of dicts: { 'car': Car, 'commands': 'FFL' }

        self.field = Field(field_width, field_heights)

        self.car_data = car_data_list

        # this was added to store car positions later
        self.positions = {}  


    def run(self):
        # checking for the the longest command length among all cars, added by user
        steps_max = max(len(c['commands']) for c in self.car_data)


""" Runs the simulation: this function will executes the rotation of every cars while iterating through each stemp. 
when the car collied then the cars stops and then update the cars position again and then show the infomration of 
collition and final state"""

        for step in range(steps_max): 

            curr_posit = {}  

            for data in self.car_data:
                car = data['car']
                commands = data['commands']

                if not car.active or step >= len(commands): 
                    continue  

                command = commands[step]  #get commend for the current step

                if command == 'L':
                    car.rotate_left() # rotate to left function calling

                elif command == 'R':
                    car.rotate_right()  # rotate to left function calling

                elif command == 'F': # get next position
                    next_x, next_y = car.move_forward()

                   
                    if not self.field.is_within_bounds(next_x, next_y):
                        continue   

                    # checking if any other car is already at that spot
                    for other in self.car_data:
                        if other == data or not other['car'].active:
                            continue # ignoring by self and dead cars

                        ox, oy, _ = other['car'].get_position()
                        
                        
                        #collision will detected here
                        if next_x == ox and next_y == oy:
 
                           
                            car1_name = car.Carname  # get name of car that is moving
                            car2_name = other['car'].Carname   # get name of the other car it crashed into         
                            collision_x = next_x                  # x coordinates where they both hit
                            collision_y = next_y                  # y coocoordinats where the car both hit
                            collision_step = step + 1               # step number (1-indexed, looks better)

                            
                            print(f"- {car1_name}, collides with {car2_name} at ({collision_x},{collision_y}) at step {collision_step}")

                          
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
                print(f"- {car.Carname}, ({car.x},{car.y}) {car.direction}")

