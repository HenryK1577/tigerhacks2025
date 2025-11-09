import nodal_logistics

mynodes = nodal_logistics.populate_galaxy(verbose = True)

print(f"Populated {len(mynodes)} nodes")

for i in range(10):
    print(mynodes[i])


nodal_logistics.build_edges(mynodes, 100, verbose = True)

print(mynodes[0])