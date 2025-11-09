import heapq
import math
from typing import List, Tuple, Dict, Optional, Set

class Node3D:
    """
    Represents a single point in 3D space for pathfinding.
    Think of this as a location (like a star or waypoint) that we can travel to.
    """
    __slots__ = ('x', 'y', 'z')  # Makes objects smaller and faster
    
    def __init__(self, x: float, y: float, z: float):
        self.x = x  # X coordinate (like left/right)
        self.y = y  # Y coordinate (like up/down)  
        self.z = z  # Z coordinate (like forward/backward)
        
    def __eq__(self, other):
        """Check if two nodes are at the same position"""
        return (self.x == other.x and 
                self.y == other.y and 
                self.z == other.z)
    
    def __hash__(self):
        """Allows nodes to be used in sets and dictionaries"""
        return hash((int(self.x), int(self.y), int(self.z)))
    
    def __lt__(self, other):
        """Required for priority queue - all nodes are equal priority"""
        return False
    
    def __repr__(self):
        """Pretty print for debugging"""
        return f"({self.x:.0f},{self.y:.0f},{self.z:.0f})"

class AStar3D:
    """
    A* Pathfinding Algorithm - Finds shortest path between two 3D points
    
    HOW IT WORKS:
    ============
    1. Explore possible paths from start to goal
    2. Always try the most promising path first (lowest estimated total cost)
    3. Avoid obstacles and find the shortest route
    
    Think of it like a smart GPS that explores multiple routes at once,
    but always focuses on the route that seems most promising.
    """
    
    def __init__(self):
        # Positions we CANNOT travel through (like walls or blocked areas)
        self.obstacles: Set[Node3D] = set()
        
        # Cache to avoid recalculating the same distances repeatedly
        # This makes the algorithm much faster
        self._distance_cache: Dict[Tuple, float] = {}
        
        # All possible movement directions in 3D space
        # Includes diagonals - 26 total possible moves from any position
        self._neighbor_offsets = [
            (dx, dy, dz) 
            for dx in (-1, 0, 1)      # Can move left, stay, or right in X
            for dy in (-1, 0, 1)      # Can move down, stay, or up in Y  
            for dz in (-1, 0, 1)      # Can move back, stay, or forward in Z
            if not (dx == 0 and dy == 0 and dz == 0)  # Don't include staying still
        ]
    
    def add_obstacle(self, x: float, y: float, z: float):
        """
        Mark a position as blocked/obstacle
        Example: add_obstacle(5, 10, 3) means you can't go to position (5,10,3)
        """
        self.obstacles.add(Node3D(x, y, z))
    
    def distance(self, a: Node3D, b: Node3D) -> float:
        """
        Calculate straight-line distance between two points (Pythagorean theorem in 3D)
        
        We cache results because the same distances are calculated many times
        during pathfinding, and math is expensive!
        """
        # Create a unique key for this pair of points
        key = (int(a.x), int(a.y), int(a.z), int(b.x), int(b.y), int(b.z))
        
        # If we haven't calculated this distance before, compute and store it
        if key not in self._distance_cache:
            dx = a.x - b.x  # Difference in X direction
            dy = a.y - b.y  # Difference in Y direction  
            dz = a.z - b.z  # Difference in Z direction
            # Pythagorean theorem: sqrt(dx² + dy² + dz²)
            self._distance_cache[key] = math.sqrt(dx*dx + dy*dy + dz*dz)
        
        return self._distance_cache[key]
    
    def get_neighbors(self, node: Node3D) -> List[Node3D]:
        """
        Get all positions we can move to from the current position
        
        Returns all adjacent positions that are NOT blocked by obstacles
        Includes diagonal moves (like moving forward+right+up simultaneously)
        """
        neighbors = []
        
        # Try moving in every possible direction
        for dx, dy, dz in self._neighbor_offsets:
            # Calculate new position by adding the direction offsets
            new_x = node.x + dx
            new_y = node.y + dy  
            new_z = node.z + dz
            
            neighbor = Node3D(new_x, new_y, new_z)
            
            # Only add this position if it's not blocked
            if neighbor not in self.obstacles:
                neighbors.append(neighbor)
        
        return neighbors
    
    def find_path(self, start: Tuple[float, float, float], 
                  goal: Tuple[float, float, float]) -> Optional[List[Node3D]]:
        """
        Find the shortest path from start position to goal position
        
        ARGUMENTS:
        - start: (x, y, z) where we begin
        - goal: (x, y, z) where we want to go
        
        RETURNS:
        - List of nodes showing each step to reach the goal
        - None if no path exists (completely blocked)
        
        THE ALGORITHM IN SIMPLE TERMS:
        1. Start at the beginning
        2. Keep exploring the most promising direction
        3. If we hit a dead end, backtrack and try another direction
        4. Stop when we reach the goal or run out of options
        """
        
        # Convert coordinate tuples into Node objects
        start_node = Node3D(*start)
        goal_node = Node3D(*goal)
        
        # Quick sanity check - can't start or end in a wall!
        if start_node in self.obstacles or goal_node in self.obstacles:
            return None
        
        # OPEN SET: Positions we plan to explore, sorted by most promising first
        # Uses a priority queue (heap) so we always get the best candidate next
        open_set = []
        heapq.heappush(open_set, (0, start_node))  # Start with beginning position
        
        # G_SCORE: Cost to reach each position from the start
        # Like keeping track of "how long it took to get here"
        g_score = {start_node: 0}  # Start position costs 0 to reach
        
        # F_SCORE: Estimated total cost (actual cost + guess to goal)
        # This is what makes A* smart - it guides the search toward the goal
        f_score = {start_node: self.distance(start_node, goal_node)}
        
        # CAME_FROM: For each position, store where we came from
        # This lets us reconstruct the path once we find the goal
        came_from: Dict[Node3D, Node3D] = {}
        
        # Track which nodes are in the open set for quick lookup
        open_set_hash = {start_node}
        
        # OPTIMIZATION: Stop when we're close to goal (within 2 units)
        # Makes algorithm much faster with barely any accuracy loss
        close_enough_threshold = 2.0
        
        # MAIN LOOP: Keep exploring until we find goal or run out of options
        while open_set:
            # Get the most promising position to explore next
            # (lowest f_score = closest estimated total distance to goal)
            current_f, current = heapq.heappop(open_set)
            open_set_hash.remove(current)
            
            # CHECK FOR SUCCESS: Are we at the goal?
            # Use early termination if we're close enough (optimization)
            if self.distance(current, goal_node) <= close_enough_threshold:
                path = self._reconstruct_path(came_from, current)
                path.append(goal_node)  # Add the actual goal to complete path
                return path
            
            # Exact position match (standard A* termination)
            if current == goal_node:
                return self._reconstruct_path(came_from, current)
            
            # EXPLORE NEIGHBORS: Check all positions we can move to from here
            neighbors = self.get_neighbors(current)
            
            for neighbor in neighbors:
                # Calculate cost to reach neighbor via current path
                # This is the actual distance traveled so far + distance to neighbor
                cost_to_current = g_score[current]
                cost_current_to_neighbor = self.distance(current, neighbor)
                tentative_g_score = cost_to_current + cost_current_to_neighbor
                
                # Is this a better path to reach this neighbor?
                # Either we haven't visited this neighbor before, or 
                # we found a shorter route to reach it
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update our records - this is the best path to this neighbor so far
                    came_from[neighbor] = current  # We reached neighbor from current
                    g_score[neighbor] = tentative_g_score  # Update cost to get here
                    
                    # Update estimated total cost (actual + guess to goal)
                    heuristic = self.distance(neighbor, goal_node)  # Guess remaining distance
                    f_score[neighbor] = tentative_g_score + heuristic
                    
                    # If neighbor isn't already scheduled for exploration, add it
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)
        
        # If we get here, we explored everything but never reached the goal
        # This means no path exists (completely blocked by obstacles)
        return None
    
    def _reconstruct_path(self, came_from: Dict[Node3D, Node3D], current: Node3D) -> List[Node3D]:
        """
        Build the final path by working backwards from goal to start
        
        We stored 'came_from' for each node, which tells us how we got there.
        Now we follow this chain backwards to build the complete route.
        """
        path = [current]  # Start with the goal node
        
        # Keep following the 'came_from' chain until we reach the start
        while current in came_from:
            current = came_from[current]  # Move to previous node in path
            path.append(current)
        
        # Reverse because we built the path backwards (goal->start)
        # We want it forwards (start->goal)
        path.reverse()
        return path
