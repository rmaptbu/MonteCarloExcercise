from MCE import MonteCarlo
def test_MonteCarlo():
	""" Testing Monte Carlo functionality """
	from diffusion_model import energy	#use diffusion model energy function as test for functionality of MC minimisation
	import nose.tools
	from nose.tools import assert_equal
	from nose.tools import assert_true
	from random import randint
	import random
	import matplotlib.pyplot as plt
	
	#minimum energy state doesn't change at absolute zero
	for n in range (3): #try three times
		density=[1.0,1.0,1.0,1.0]
		density=MonteCarlo ("diffusion_model","energy",density,0)
		assert_equal(density,[1.0,1.0,1.0,1.0])
	
	#energy state lowers until minimum energy state is reached at absolute zero or iterated 100 times
	density=range(10)
	for i in range (10):
		density[i]=random.randint(1,10) #fill density with random integers
	if max(density)-min(density)<=1:
		density_backup=density[:]
		MonteCarlo("diffusion_model","energy",density,0)
		assert_true(density=density_backup)
	else:
		E0=energy(density)
		x=100
		MCEnergy=[]
		while (max(density)-min(density)>=2) and x>0: #if distribution is non-uniform energy minimum is not reached
			MCEnergy.append(energy(density))
			density=MonteCarlo("diffusion_model","energy",density,0)
			x-=1
		print "energy changed by ", MCEnergy
		plt.plot(MCEnergy)
		plt.show()
	assert_true(E0>energy(density))
		
