def MonteCarlo(E_module, E_function,density,temperature=0):
	""" Minimise energy of given Hamiltonian
		need input: Hamiltonian (E_module.E_function), starting point (density)
	"""
	import sys
	if E_module in sys.modules:
		print getattr(sys.modules[E_module],E_function)(density)
	else:
		raise NameError('Energy Module not loaded')
	