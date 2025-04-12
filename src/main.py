# src/main.py

from car import Car
from field import Field
from simulator import Simulator  #importing

# Ask the developer/user to enter the size of the simulation field which should be width x height.
def input_field_size():
    while True: # i used infinte loop to get the correct input
        try: # using try and catech to get the error incase of any issue 
            getInput = input("Please enter the weidth and height of the simulation field in X Y formate:\n").split()

            if len(getInput) != 2: #checking that input is get exactly two values, if not then give error
                raise ValueError

            wight, heights = map(int, getInput) #converting the heights and width into int from strings

            if wight <= 0 or heights <= 0:  #confirming that both heigth and wight is not in negative 
                raise ValueError

            return wight, heights  #return the values of width and height in form (10, 10) tupel

        except ValueError: #give error incaes of any issue
            print("Invaliad. Please type two posiitive number, like: 10 10")

# collec detail for a new car: like name, starting position, direction, and movement command
def ading_car():
    nameOfCar = input("Please enterr the name of the car:?\n").strip() #need to give car name
    while True:
        try:
            #getting starting line and direction position in 1 line like (1 2 N)
            Dirction = input(f"\nPlease enter initial position of car {nameOfCar} in x y Direction format: (x y D):\n").split()
            
            if len(Dirction) != 3 or Dirction[2] not in ['N', 'S', 'E', 'W']: #constraint to get the correct direction and 3 part like above
                raise ValueError

            x, y = int(Dirction[0]), int(Dirction[1]) # convert x, and y into number(int) and not convert dir
            dir = Dirction[2] 
            break

        except ValueError: #show message if user did something wrong like missing value or bad dir
            print("Oops. Use formate like '1 2 N'. Direction must like N, S, E, or W.")

    # asking for movements commands (F = forward, L = left, R = right) from user
    cmds = input(f"Please enter the commands for CAR {nameOfCar} (F/L/R):\n").strip().upper()

    return nameOfCar, x, y, dir, cmds     # return all info back so caller function so can use it


# Entry point of the simuletion programe
def start_simulation():
    print("\n- Welcome to Auto Driving Car Simulation! ") #wlecome message when the Simulation Starts

    # Seting the Field/gred (user can gives the width and the height)
    width, height = input_field_size()
    print(f"\nYou have To created a feild of 10 X 10. {width} x {height}")

    car_list = [] # holding all the cars added by user

    while True:
        # Menu for users for adding a car or to the run the simulation
        print("\nWhat would you like to do is?")
        print("[1] Adding a new Car")
        print("[2] Run The simuletion")
        chocie = input().strip()

        if chocie == '1':
            # collect the car info and create car object
            
            result = ading_car()  # collect informtion from user like Carname, pos, dir, cmd

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

            # Print all cars
            print("\n\n\nYour current list of cars are::")
            for c in car_list:
                All_cars = c['car']
                print(f"- {All_cars.name}, ({All_cars.x},{All_cars.y}) {All_cars.direction}, {c['commands']}")

        elif chocie == '2':
            # let user konw simulatino is about to start
            print("\n- After simulation, the results is: ")
            # pass all details and stuff to simulator class and run the simulation
            
            # first set the width for the simulation that input in start
            field_width = width

            # same for height,
            field_height = height

            # all cars that user added are already in car list
            all_cars = car_list

            # now create the simulator objct with all the infromation
            executing = Simulator(width, height, car_list)
            executing.run()  # this would show moves and collisions of the cars

            #RestarT or exit commands
            print("\n\nPlease choose from the following options: \n\n")
            print("\n[1] Start Over")  # restart everything
            print("[2] Exit") # exit the appliction

             # take user input again
            again = input().strip()

            if again == '1': # if u/user chose to start again, call the same main function
                start_simulation()
            else:
                 # any other option will end the application with goodbye output
                print("\nThank you for running the simulation. Goodbye!")
                break

        else:
            # if user can enter something that isn't 1 or 2
            print("Invalid option. Type 1 or 2.")


if __name__ == "__main__": # this is the main function to check
    start_simulation()  # if user runs this file directly, start the whole sim
