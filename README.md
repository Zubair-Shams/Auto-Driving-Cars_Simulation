# Auto Driving Car Simulation

This project simulates how cars move in a rectangular grid like how autonomous driving systems might work. The goal is to create a basic simulation where multiple cars move around inside a box, follow instructions, and stop if they crash car into each other.

---

## How It Works

- The program starts by asking you to enter the field size (like a grid or box).  
  Example: `10 10` means a 10x10 field size.

- Then, you can add one or more cars. For each car, you'll enter:
  - A name (like `A`, `B` etc)
  - Starting position (e.g., `1 2 N`)
  - A direction (`N`, `S`, `E`, or `W`) — which means North, South, East, or West
  - A command string that tells the car how to move

### Command Instructions:
- `F` = Move forward one step  
- `L` = Turn left  
- `R` = Turn right

---

## How Simulation Runs

- After all cars are added, the simulation starts
- Each car runs **one command at a time per step**
- If two cars end up in the **same spot at the same step**, they are marked as **collided** and stop moving

---

## How to Run

1. Make sure Python is installed
2. Open terminal and go to the `src` folder
3. Run this command:

```bash
python main.py
