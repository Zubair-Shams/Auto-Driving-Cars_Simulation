# src/main.py

from car import Car
from field import Field
from simulator import Simulator# importing



def input_field_size():
    """
    Ask the user to enter the size of the field (width and height).
    Loops until valid input. Converts strings to integers.
    Checks that values are positive.
    Returns a tuple (width, height).
    """
    while True:
        try:
            getInput = input("Please enter the width and height of the simulation field in X Y format:\n").split()

            if len(getInput) != 2:
                raise ValueError

            width, height = map(int, getInput)

            if width <= 0 or height <= 0:
                raise ValueError

            return width, height

        except ValueError:
            print("Invalid. Please enter two positive numbers, like: 10 10")


def ading_car():
    """
    Collect details for a new car:
    - Name
    - Starting position (x, y)
    - Direction (N, E, S, W)
    - Movement commands (F, L, R)
    """
    nameOfCar = input("Please enter the name of the car:\n").strip()

    while True:
        try:
            Dirction = input(f"\nPlease enter initial position of car {nameOfCar} in x y Direction format: (x y D):\n").split()

            if len(Dirction) != 3 or Dirction[2] not in ['N', 'S', 'E', 'W']:
                raise ValueError

            x, y = int(Dirction[0]), int(Dirction[1])
            dir = Dirction[2]
            break

        except ValueError:
            print("Oops. Use format like '1 2 N'. Direction must be N, S, E, or W.")

    cmds = input(f"Please enter the commands for CAR {nameOfCar} (F/L/R):\n").strip().upper()
    return nameOfCar, x, y, dir, cmds


def start_simulation():
    print("\n- Welcome to Auto Driving Car Simulation!")

    width, height = input_field_size()
    print(f"\nYou have created a field of {width} x {height}")

    car_list = []

    while True:
        print("\nWhat would you like to do?")
        print("[1] Add a new Car")
        print("[2] Run the simulation")
        choice = input().strip()

        if choice == '1':
            result = ading_car()

            Carname = result[0]
            x = result[1]
            y = result[2]
            dir = result[3]
            cmds = result[4]

            new_car = Car(Carname, x, y, dir)

            car_list.append({
                'car': new_car,
                'commands': cmds
            })

            print("\nYour current list of cars are:")
            for c in car_list:
                this_car = c['car']
                print(f"- {this_car.Carname}, ({this_car.x},{this_car.y}) {this_car.direction}, {c['commands']}")

        elif choice == '2':
            print("\n- Running the simulation...")

            executing = Simulator(width, height, car_list)
            executing.run()

            print("\nPlease choose from the following options:")
            print("[1] Start Over")
            print("[2] Exit")

            again = input().strip()

            if again == '1':
                break
            else:
                print("\nThank you for running the simulation. Goodbye!")
                return

        else:
            print("Invalid option. Type 1 or 2.")



if __name__ == "__main__":
    start_simulation()
