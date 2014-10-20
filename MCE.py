def MonteCarlo(E,density,temperature=0):
	""" Minimise energy of given Hamiltonian
		need input: Hamiltonian (energy), starting point (density)
	"""
	from diffusion_model import energy
	if E in locals():
		locals()[E](density)
	else:
		raise NameError('energy function not found')

MonteCarlo ("energy",[2.0, 1.0])