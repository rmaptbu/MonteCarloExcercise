def MonteCarlo(E_module, E_function,density,temperature=1):
	""" ONE STEP towards minimising energy of given Hamiltonian
		need input: Hamiltonian (E_module.E_function), starting point (density)
	"""
	import sys
	import random
	from numpy import exp
	from random import randrange
	if E_module in sys.modules:						#does module exist?
		Energy=getattr(sys.modules[E_module],E_function)	#set function "energy" as hamiltonian
		temp_density=density[:]
		E0=Energy(temp_density)
		
		particle=randrange(0,len(temp_density))		#select random particle
		if temp_density[particle] >= 1:				#move particle away if it exists
			temp_density[particle]-=1
			print "particle position ", particle
			if particle>0 and particle<(len(temp_density)-1):
			#place particle randomly to the left or right if the outermost particle wasnt removed
				if bool(random.getrandbits(1)):	
					temp_density[particle+1]+=1
				else:
					temp_density[particle-1]+=1
			#place particle to the left/right if last or first particle was removed respectively
			elif particle==0:
				temp_density[particle+1]+=1
			else:
				temp_density[particle-1]+=1
		E1=Energy(temp_density)
		
		print "density0 is ", density
		print "density1 is  ", temp_density
		
		if E1>E0 and exp(-(E1-E0)/temperature)<random.random(): #change passed
			density=temp_density
			print "step accepted"
		else:
			print "step not accepted"
		
	else:
		raise NameError('Energy Module not loaded')
	