import nodal_logistics

mynodes = nodal_logistics.populate_galaxy(verbose = True)

print(f"Populated {len(mynodes)} nodes")

for i in range(10):
    print(mynodes[i])