# Python script to compute links inertia from material density and mesh file
import trimesh
import numpy as np

# Compute TITAN 4 Inertia: 
density = 4.5  #[g/cm^3]

arm_links = ["arm_base", "arm_link1", "arm_link2", "arm_link3", "arm_link4", "arm_link5", "grip_claw", "grip_claw"]
volume = []
mass = []
CoM = []
inertia_matrix = []

i = 0
for link in arm_links:
    stl_file = "/home/ale/ros2_ws/src/rov_ricketts_description/meshes/" + link + ".stl"
    mesh = trimesh.load(stl_file)
    volume.append(mesh.volume) # [m^2]
    mass.append(mesh.volume*(density*1000)) # [Kg]
    CoM.append(mesh.center_mass) #(1x3) [m]
    # inertia_matrix.append(mesh.moment_inertia) #(3x3) [Kg*m^2/kg] Scaled Inertia
    inertia_matrix.append(mesh.moment_inertia*mass[i]) # (3x3) [Kg*m^2] 

    print(f"\nLink {link}: \n Volume= {volume[i]}\nMass= {mass[i]}\nCenter of Mass= {CoM[i]}\nInertia Matrix= {inertia_matrix[i]}\n------------------")
    i+=1

print("\ntotal mass: " + str(sum(mass)))