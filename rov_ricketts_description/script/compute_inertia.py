# Python script to compute links inertia from material density and mesh file
import trimesh
import numpy as np
from ament_index_python.packages import get_package_share_directory

# Compute TITAN 4 Inertia: 
density = 4.5  #[g/cm^3]

arm_links = ["arm_base", "arm_link1", "arm_link2", "arm_link3", "arm_link4", "arm_link5", "grip_claw", "grip_claw"]
volume = []
mass = []
CoM = []
inertia_matrix = []

i = 0
for link in arm_links:
    mesh_path = get_package_share_directory('rov_ricketts_description')
    stl_file = mesh_path + "/meshes/" + link + ".stl"
    mesh = trimesh.load(stl_file)
    volume.append(mesh.volume)              # [m^2]
    mass.append(mesh.volume*(density*1000)) # [Kg]
    CoM.append(mesh.center_mass)            # [m] (1x3)
    # inertia_matrix.append(mesh.moment_inertia) # [(Kg*m^2)/(kg*m^3)] (3x3) Normalized Inertia
    inertia_matrix.append(mesh.moment_inertia*mass[i]/volume[i]) # (3x3) [Kg*m^2] 

    print(f"\nLink {link}: \n Volume= {volume[i]}\nMass= {mass[i]}\nCenter of Mass= {CoM[i]}\nInertia Matrix= {inertia_matrix[i]}\n------------------")
    i+=1

print("\ntotal mass: " + str(sum(mass)))