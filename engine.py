class SokobanState:
    def __init__(self, player, boxes, targets, walls):
        self.player = player          # (x, y)
        self.boxes = frozenset(boxes) # Set of (x, y)
        self.targets = frozenset(targets)
        self.walls = frozenset(walls)

    def is_goal(self):
        return self.boxes == self.targets

    def __hash__(self):
        return hash((self.player, self.boxes))

    def __eq__(self, other):
        return self.player == other.player and self.boxes == other.boxes

def is_corner_deadlock(box, walls, targets):
    if box in targets:
        return False
    x, y = box
    top = (x, y - 1) in walls
    bottom = (x, y + 1) in walls
    left = (x - 1, y) in walls
    right = (x + 1, y) in walls
    return (top and left) or (top and right) or (bottom and left) or (bottom and right)

def get_successors(state):
    successors = []
    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    
    for action, (dx, dy) in directions.items():
        nx, ny = state.player[0] + dx, state.player[1] + dy
        new_player = (nx, ny)
        
        if new_player in state.walls:
            continue
            
        new_boxes = set(state.boxes)
        if new_player in new_boxes:
            push_x, push_y = nx + dx, ny + dy
            new_box_pos = (push_x, push_y)
            
            if new_box_pos in state.walls or new_box_pos in new_boxes:
                continue
                
            if is_corner_deadlock(new_box_pos, state.walls, state.targets):
                continue
                
            new_boxes.remove(new_player)
            new_boxes.add(new_box_pos)
            
        successors.append((action, SokobanState(new_player, new_boxes, state.targets, state.walls)))
        
    return successors