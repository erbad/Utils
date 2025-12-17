import mdtraj as md
import numpy as np

# Supported trajectory formats:
# pdb, xtc, trr, dcd, binpos, netcdf, mdcdr, prmtop


# Load import a trajectory in whatever extension.
# If the trajectory doesn't have topology information, then we give it with 'top'.
t = md.load('traj.xtc', top='top.pdb')
print(t)

# Features of the trajectory:
t.n_atoms
t.n_residues
top = t.topology


# TRAJECTORY

# Select the first ten frames.
t[1:10]


# Select the last frame.
t[-1]


# Coordinates are saved in 'xyz' array
print(t.xyz.shape) # Returns (# frames, # atoms, # coordinates).
print(np.mean(t.xyz)) # Returns the average of al coordinates of all atoms along the whole simulation. 


# Simulation time (in ps) is saved in the time array
print(t.time[0:10])


# Size of the simulation cell is stored in
t.unitcell_lengths[T] # T in the frame


# To save a trajectory back to the disk we use 'save':
t.save('out.XXX')
t[::2].save('out-x2.XXX') # to save one frame every 2.
# With the format '.h5' the topology is saved inside the file.

# There are extension-specific saver:
t[0:10].save_dcd('out.dcd')


# We can select only some atoms to rewrite the trajectory:
carbon_alpha = [a.index for a in t.topology.atoms if a.name == 'CA']
t.restrict_atoms(carbon_alpha)
t.save('carbon-alpha.XXX')


# TOPOLOGY

# Residues and atoms start at 0, we can select them all with the plural:
top.atom(4)     # fifth atom
top.residue(6)  # seventh residue
top.atoms       # all atoms
top.residues    # all residues


# From topology we can select atoms based on keywords:
top.select('name CA')       # all CA atoms
top.select('index 2 to 8')  # from third to ninth atoms
top.select('resid 1 to 5')  # from second to sixth
top.select('resname ALA')   # all alanines
top.select('chainid 0-3')   # all chains from the first to the fourth
top.select('backbone')      # backbone atoms
top.select('sidechain')     # sidechain atoms
top.select('protein')
top.select('water')
# They can be even combined - e.g.:
top.select('name CA and resid 0 to 10')
top.select('protein and (backbone or resname ALA)')



