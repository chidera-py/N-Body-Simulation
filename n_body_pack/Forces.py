import numpy as np

class Force:
	def lj_force(r):
	"""Calculate Lennard-Jones force between particles"""
	v_lj = 4 * ( (1/r)**12 - (1/r)**6)
	return v_lj

	def net_force(particle_i, N):
	"""Calculate net force from i to j"""
	
	net_force = 0
	for particle_j in N:
		if particle_j == particle_i:
			continue
	rij = (particle_j.positon - particle_i.position)
	r = np.linalg.norm(rij) 
		
	net_force += 24*(-2(1/r)**13 + (1/r)**7) * (rij/r)
	return net_force

	def check_wall_collision(particle, grid_size =None):
	"""Check for collisons if box size is given"""
	if grid_size is not None:
		#implement collision detecteion
		pass
	else:
		return	
