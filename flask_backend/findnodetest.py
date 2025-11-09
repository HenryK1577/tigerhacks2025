import find_nodes as fn
import nodal_logistics as nl

goal = (151.57118907224933, -366.8982680493465, 415.26064570292993)
print(f"Attempt to find {goal}...")

p_string = fn.find_path(goal, 100)

print(p_string)

# node_graph = nl.get_graph_cache()
# node_graph = nl.filter_octant(goal, node_graph)

# print(f"Nodes after filtering: {len(node_graph)}")

# node_graph.insert(0, nl.SystemNode((0, 0, 0), "Earth"))
# nl.build_edges(node_graph, 100)
# print("Edges built")

# start = node_graph[0]
# print(f"Earth: {str(start)}")

# goal = next(
#         (node for node in node_graph
#             if abs(node.x - goal[0]) < 1e-6
#             and abs(node.y - goal[1]) < 1e-6
#             and abs(node.z - goal[2]) < 1e-6),
#             None)
    
# print(f"Goal: {str(goal)}")

# path = fn.astar(start, goal)

# if path:
#     p_string = "Path found:\n"
#     for step in path:
#         p_string += f"{step} \n"
#     print(p_string)  
# else:
#     print("No path found")
