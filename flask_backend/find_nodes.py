import nodal_logistics as nl
from nodal_logistics import SystemNode
import riaziAstar

import heapq
import math

def find_path(goal_coords: tuple, max_distance: float = 100, verbose = False):
    node_graph = nl.get_graph_cache()
    node_graph = nl.filter_octant(goal_coords, node_graph)

    verbose and print(f"Nodes after filtering: {len(node_graph)}")

    node_graph.insert(0, nl.SystemNode((0, 0, 0), "Earth"))
    nl.build_edges(node_graph, max_distance)
    verbose and print("Edges built")

    start = node_graph[0]
    print(f"Earth: {str(start)}")

    goal = next(
            (node for node in node_graph
                if abs(node.x - goal_coords[0]) < 1e-6
                and abs(node.y - goal_coords[1]) < 1e-6
                and abs(node.z - goal_coords[2]) < 1e-6),
                None)
        
    print(f"Goal: {str(goal)}")

    path = astar(start, goal)

    if path:
        first = 1
        p_string = "Path found:\n"
        for step in path:
            if first ==1:
                first = 0
                p_string+= f"From {step}"
            else:
                p_string += f"to {step} \n"
        return p_string
    else:
        return "No path found"


    # node_graph = nl.get_graph_cache()
    # node_graph = nl.filter_octant(goal_coords, node_graph)
    # node_graph.insert(0, SystemNode((0, 0, 0), "Earth"))
    # nl.build_edges(node_graph, max_distance)


    # start = node_graph[0]

    # goal = next(
    #     (node for node in node_graph
    #         if abs(node.x - goal_coords[0]) < 1e-6
    #         and abs(node.y - goal_coords[1]) < 1e-6
    #         and abs(node.z - goal_coords[2]) < 1e-6),
    #         None)
    
    # path = astar(start, goal)

    # if path:
    #     p_string = "Path found:\n"
    #     for step in path:
    #         p_string += f"{step} \n"
    #         return p_string
    # else:
    #     return "No path found"
    


    

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(start_node, goal_node):
    # Priority queue for (f_cost, node)
    open_set = []
    heapq.heappush(open_set, (0, start_node))

    came_from = {}               # For reconstructing path
    g_score = {start_node: 0}    # Actual cost to reach node

    while open_set:
        _, current = heapq.heappop(open_set)

        # Goal reached
        if current is goal_node:
            return reconstruct_path(came_from, current)

        # Explore neighbors
        for neighbor in current.connections:
            tentative_g = g_score[current] + nl.node_dist(current, neighbor)

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                # f = g + h
                f_cost = tentative_g + nl.node_dist(neighbor, goal_node)
                heapq.heappush(open_set, (f_cost, neighbor))

    return None  # No path found


