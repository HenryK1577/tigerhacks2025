import nodal_logistics

mynodes = nodal_logistics.populate_galaxy(verbose = True)

print(f"Populated {len(mynodes)} nodes")

for i in range(10):
    print(mynodes[i])

mynodes = nodal_logistics.filter_octant(mynodes[2].coords, mynodes)

print(f"Filtered to {len(mynodes)} nodes")

nodal_logistics.build_edges(mynodes, 100, verbose = True)

print(mynodes[0])
#mynodes[0].print_edges()