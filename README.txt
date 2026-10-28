# Sokoban AI Solver: AO* Search Algorithm

## Project Overview
This project is an automated AI solver for the classic puzzle game Sokoban. It mathematically maps a 2D text-based grid into a discrete state-space matrix and utilizes the **AO* (AND-OR) Search Algorithm** to find the optimal sequence of moves. The solver demonstrates complex problem decomposition, heuristic-driven pathfinding (Means-Ends Analysis), and search-space pruning to handle the game's PSPACE-complete complexity. The final solution is animated in real-time using a Pygame interface while the internal decision matrix is logged to the terminal.

## Core Features
* **Sub-Goal Decomposition (AND/OR Graph):** Evaluates alternative directional paths (OR conditions) while calculating the cost to simultaneously route multiple independent boxes to their respective targets (AND conditions).
* **Means-Ends Analysis Heuristic:** Uses Manhattan distance calculations to evaluate the physical difference between the current board state and the goal state, guiding the AI toward the most efficient moves.
* **Deadlock Pruning:** Automatically detects corner-wedged boxes and immediately abandons impossible search branches to drastically reduce memory consumption and execution time.
* **Dual Visualization:** Outputs a hierarchical text-based search tree and 2D mathematical matrix to the terminal to prove internal logic, while simultaneously animating the physical sprites via Pygame.

## Project Structure
* `main.py` — The central controller. Parses the ASCII level grid, triggers the search algorithm, logs the performance time, and launches the graphical playback.
* `engine.py` — The strict mathematical rulebook. Defines the `SokobanState` class, handles coordinate vector addition for movement, and generates valid future board states (`get_successors`).
* `ao_star.py` — The AI brain. Contains the heuristic calculations, the `AONode` priority queue sorting logic, and the recursive tree-printing function.
* `gui.py` — The visualizer. Translates the calculated coordinate sequence into an animated sequence using the Pygame graphics library.

## Installation & Setup

1. **Clone the repository or download the project files.** Ensure all four Python files are located in the same directory.
2. **Install the required dependencies.** The algorithm runs on standard Python libraries, but the visualizer requires Pygame.
   ```bash
   pip install pygame

Execution
Run the main controller script from your terminal:

Bash
python main.py
Example Levels for Testing

To test the AI on different puzzles, open main.py and modify the multiline string variable named level. Replace it with any of the easy layouts below.

(Key: # = Wall, @ = Player, $ = Box, . = Target, * = Box on Target, + = Player on Target)

Level 1: The Basics (1 Box)
Plaintext
######
#    #
# @$ #
#  . #
######
Level 2: The Corridor (2 Boxes)
Plaintext
#######
#     #
# .$. #
#  @  #
#  $  #
#     #
#######
Level 3: The Corner Push (3 Boxes)
Plaintext
########
#      #
# . $  #
# . $@ #
# . $  #
#      #
########