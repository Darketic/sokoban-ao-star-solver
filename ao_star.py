from engine import get_successors

def calculate_heuristic(boxes, targets):
    # Simplified Means-Ends Distance (Manhattan)
    total_cost = 0
    remaining_targets = list(targets)
    for box in boxes:
        if box in remaining_targets:
            remaining_targets.remove(box)
            continue
        distances = [abs(box[0] - t[0]) + abs(box[1] - t[1]) for t in remaining_targets]
        total_cost += min(distances) if distances else 0
    return total_cost

class AONode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.children = [] # Tracks explored branches for the tree printout
        self.action = action
        self.h = calculate_heuristic(state.boxes, state.targets)
        self.g = 0 if parent is None else parent.g + 1
        self.f = self.g + self.h
        
        if parent:
            parent.children.append(self) # Link child to parent

    def __lt__(self, other):
        # Tells the priority queue to sort by the lowest total cost (f)
        return self.f < other.f

def print_search_tree(node, depth=0, max_depth=3):
    if not node or depth > max_depth:
        return
        
    indent = "  " * depth
    move = f"Move {node.action}" if node.action else "Start"
    print(f"{indent}├─ {move} (Cost: {node.f})")
    
    for child in node.children:
        print_search_tree(child, depth + 1, max_depth)

def ao_star_search(initial_state):
    from heapq import heappush, heappop
    
    open_list = []
    closed_set = set()
    
    root = AONode(initial_state)
    heappush(open_list, root)
    
    while open_list:
        current = heappop(open_list)
        
        if current.state.is_goal():
            path = []
            while current.parent:
                path.append(current.action)
                current = current.parent
                
            # Print the tree right before returning the solution
            print("\n--- Final Search Tree ---")
            print_search_tree(root, max_depth=4) 
            
            return path[::-1]
            
        if current.state in closed_set:
            continue
            
        closed_set.add(current.state)
        
        for action, next_state in get_successors(current.state):
            if next_state not in closed_set:
                child_node = AONode(next_state, current, action)
                current.children.append(child_node) # Ensure nodes are linked
                heappush(open_list, child_node)
                
    return None