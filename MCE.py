def MonteCarlo(E_module, E_function,density,temperature=0):
	""" Minimise energy of given Hamiltonian
		need input: Hamiltonian (E_module.E_function), starting point (density)
	"""
	import sys
	import random
	import numpy
	from random import randrange
	if E_module in sys.modules:
		Energy=getattr(sys.modules[E_module],E_function)	#set function "energy" as hamiltonian
		E0=Energy(density)
		
		particle=randrange(0,len(density))		#select random particle
		if density[particle] >= 1:				#move particle away if it exists
			density[particle]-=1							
			if bool(random.getrandbits(1)):		#place particle to the left or right
				density[particle+1]+=1
			else:
				density[particle-1]+=1
		E1=Energy(density)
		
		print "E0 is ", E0
		print "E1 is ", E1
		
		if E1>E0 and exp(-(E1-E0)/temperature)<random.random()
		
	else:
		raise NameError('Energy Module not loaded')
	