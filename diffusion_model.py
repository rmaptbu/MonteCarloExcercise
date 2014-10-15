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
  
	E=0.0
	for i in range(len(density)-1):
		E += density[i+1]*density[i]
	E*=D/2.0
	print E
	return E
	
energy ([5.0, 6.0],1.0)
