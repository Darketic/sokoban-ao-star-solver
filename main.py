import time
from engine import SokobanState
from ao_star import ao_star_search
from gui import play_gui

def parse_level(level_str):
    walls, boxes, targets = set(), set(), set()
    player = None
    
    lines = level_str.strip('\n').split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            elif char == '@':
                player = (x, y)
            elif char == '$':
                boxes.add((x, y))
            elif char == '.':
                targets.add((x, y))
            elif char == '*':
                boxes.add((x, y))
                targets.add((x, y))
            elif char == '+':
                player = (x, y)
                targets.add((x, y))
                
    return SokobanState(player, boxes, targets, walls), len(max(lines, key=len)), len(lines)

if __name__ == "__main__":
    # A slightly more complex solvable level to watch the AI work
    level ="""
  ########
  ###   ##
  #.@$  #
  ### $.#
  #.##$ #
  # # . #
  #$ *$$.#
  #   .  #
  ########
"""
    initial_state, width, height = parse_level(level)
    
    print("Starting AO* Sub-Goal Decomposition Search...")
    start_time = time.time()
    solution = ao_star_search(initial_state)
    
    if solution:
        print(f"Solved in {time.time() - start_time:.4f} seconds!")
        print(f"Solution Path ({len(solution)} steps): {''.join(solution)}")
        print("Launching Pygame interface...")
        play_gui(initial_state, solution, width, height)
    else:
        print("No solution found. Check level design or deadlock logic.")

def print_matrix(state, width, height):
    print("\nCurrent State Matrix:")
    for y in range(height):
        row = []
        for x in range(width):
            pos = (x, y)
            if pos in state.walls: row.append('[ # ]')
            elif pos == state.player: row.append('[ @ ]')
            elif pos in state.boxes: row.append('[ $ ]')
            elif pos in state.targets: row.append('[ . ]')
            else: row.append('[   ]')
        print("".join(row))
    print("-" * (width * 5))