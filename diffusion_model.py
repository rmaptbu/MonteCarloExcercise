def energy(density, D=1.0):
	""" Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
	"""
	# implementation goes here
	from numpy import array, any, sum
	density=array(density)
	E=0.0
	E=sum(density*(density - 1))
	E*=D/2.0
	return E
	

