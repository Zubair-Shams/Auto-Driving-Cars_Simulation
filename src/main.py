# src/main.py

from car import Car
from field import Field
from simulator import Simulator  #importing
    """
    Ask the developer/user to enter the size of the simulation field which should be width x height.
    i used infinte loop to get the correct input
    using try and catech to get the error incase of any issue 
    checking that input is get exactly two values, if not then give error
    converting the heights and width into int from strings
    confirming that both heigth and wight is not in negative 
    return the values of width and height in form (10, 10) tupel
    give error incaes of any issue
    """
def input_field_size():

    while True:
        try: 
            getInput = input("Please enter the weidth and height of the simulation field in X Y formate:\n").split()

            if len(getInput) != 2:
                raise ValueError

            wight, heights = map(int, getInput) 

            if wight <= 0 or heights <= 0:  
                raise ValueError

            return wight, heights  

        except ValueError: 
            print("Invaliad. Please type two posiitive number, like: 10 10")

    """
    collec detail for a new car: like name, starting position, direction, and movement command
    need to give car name
    getting starting line and direction position in 1 line like (1 2 N)
    constraint to get the correct direction and 3 part like above
    convert x, and y into number(int) and not convert dir
    show message if user did something wrong like missing value or bad dir
    asking for movements commands (F = forward, L = left, R = right) from user
    return all info back so caller function so can use it
    """
def ading_car():
    nameOfCar = input("Please enterr the name of the car:?\n").strip() 
    while True:
        try:
            
            Dirction = input(f"\nPlease enter initial position of car {nameOfCar} in x y Direction format: (x y D):\n").split()
            
            if len(Dirction) != 3 or Dirction[2] not in ['N', 'S', 'E', 'W']: 
                raise ValueError

            x, y = int(Dirction[0]), int(Dirction[1]) 
            dir = Dirction[2] 
            break

        except ValueError: 
            print("Oops. Use formate like '1 2 N'. Direction must like N, S, E, or W.")

    
    cmds = input(f"Please enter the commands for CAR {nameOfCar} (F/L/R):\n").strip().upper()

    return nameOfCar, x, y, dir, cmds     


"""
Entry point of the simulation program.
in this function use can enter the with and hight which give furteher more cars with name, position, direction and movment
Stores all added cars and their commands in a list
stroing all the cars information and run the program step by step to process for each car
this program detecting the car collision and stop the cars which are in and give functionality to restart the simulation again or exit
"""

def start_simulation():
    print("\n- Welcome to Auto Driving Car Simulation! ") 

   
    width, height = input_field_size()
    print(f"\nYou have To created a feild of 10 X 10. {width} x {height}")

    car_list = [] 

    while True:
        
        print("\nWhat would you like to do is?")
        print("[1] Adding a new Car")
        print("[2] Run The simuletion")
        chocie = input().strip()

"""collect the car info and create car object
    collect informtion from user like Carname, pos, dir, cmd
    """
        if chocie == '1':
            
            
            result = ading_car()  

            Carname = result[0]  # car name like "A" or "B"
            x = result[1]     # getting x position of the car
            y = result[2]     # geting y position of the cars
            dir = result[3]   # direction like N, S, E, W of the car
            cmds = result[4]  # movement commands like FFRL
            new_car = Car(Carname, x, y, dir)  # create the car obj from the above informetion

            # adding car to the big car list (so simlation can use later for )
            car_list.append({
                'car': new_car,
                'commands': cmds
            })

         
            print("\n\n\nYour current list of cars are::")
            for c in car_list:
                this_car = c['car']
                print(f"- {this_car.Carname}, ({this_car.x},{this_car.y}) {this_car.direction}, {c['commands']}")

        elif chocie == '2':
            
            print("\n- After simulation, the results is: ")
            
            field_width = width
            field_height = height

            # all cars that user added are already in car list
            all_cars = car_list

            # now create the simulator objct with all the infromation
            executing = Simulator(width, height, car_list)
            executing.run()  

           
            print("\n\nPlease choose from the following options: \n\n")
            print("\n[1] Start Over")  #
            print("[2] Exit") 

            
            again = input().strip()

            if again == '1': # if u/user chose to start again, call the same main function
                break  # exit inner loop and restart from the top again
            else:
                print("\nThank you for running the simulation. Goodbye!")
                return  


        else:
           
            print("Invalid option. Type 1 or 2.")


if __name__ == "__main__":
    start_simulation()  
