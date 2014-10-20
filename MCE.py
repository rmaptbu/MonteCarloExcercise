def MonteCarlo(E_module, E_function,density,temperature=0):
	""" Minimise energy of given Hamiltonian
		need input: Hamiltonian (E_module.E_function), starting point (density)
	"""
	import sys
	import random
	from random import randrange
	if E_module in sys.modules:
		Energy=getattr(sys.modules[E_module],E_function)	#set function "energy" as hamiltonian
		E1=Energy(density)
		
		particle=randrange(0,len(density))		#select random particle
		if density[particle] >= 1:				#move particle away if it exists
			density[particle]-=1							
			if bool(random.getrandbits(1)):		#place particle to the left or right
				density[particle+1]+=1
			else:
				density[particle-1]+=1
		E2=Energy(density)
		
		print "E1 is ", E1
		print "E2 is ", E2
	else:
		raise NameError('Energy Module not loaded')
	