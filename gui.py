import pygame
from engine import get_successors

# Constants and Colors
TILE_SIZE = 64
COLORS = {
    'WALL': (80, 80, 80),
    'FLOOR': (220, 220, 220),
    'TARGET': (200, 50, 50),       # Red dot
    'BOX': (150, 100, 50),         # Brown square
    'BOX_ON_TARGET': (50, 200, 50),# Green square (Solved)
    'PLAYER': (50, 50, 200)        # Blue circle
}

def draw_state(screen, state, width, height):
    screen.fill(COLORS['FLOOR'])
    
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pos = (x, y)
            
            # Draw Walls
            if pos in state.walls:
                pygame.draw.rect(screen, COLORS['WALL'], rect)
            
            # Draw Targets
            if pos in state.targets:
                pygame.draw.circle(screen, COLORS['TARGET'], rect.center, TILE_SIZE // 6)
                
            # Draw Boxes
            if pos in state.boxes:
                box_color = COLORS['BOX_ON_TARGET'] if pos in state.targets else COLORS['BOX']
                inner_rect = rect.inflate(-16, -16)
                pygame.draw.rect(screen, box_color, inner_rect)
                
            # Draw Player
            if pos == state.player:
                pygame.draw.circle(screen, COLORS['PLAYER'], rect.center, TILE_SIZE // 3)

    pygame.display.flip()

def play_gui(initial_state, solution, width, height):
    pygame.init()
    screen = pygame.display.set_mode((width * TILE_SIZE, height * TILE_SIZE))
    pygame.display.set_caption("Sokoban AO* Solver")
    
    current_state = initial_state
    draw_state(screen, current_state, width, height)
    
    # 1. Print the starting matrix
    print("\n--- Initial Matrix ---")
    print_matrix(current_state, width, height) 
    
    pygame.time.wait(1000) 
    
    running = True
    step_idx = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
        if solution and step_idx < len(solution):
            step = solution[step_idx] 
            for action, next_state in get_successors(current_state):
                if action == step:
                    current_state = next_state 
                    break
            
            draw_state(screen, current_state, width, height)
            
            # 2. Print the updated matrix after each move
            print(f"\n--- Move: {step} ---")
            print_matrix(current_state, width, height)
            
            step_idx += 1 
            pygame.time.wait(400) 
            
    pygame.quit()

def print_matrix(state, width, height):
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