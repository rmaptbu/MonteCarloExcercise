from MCE import MonteCarlo
def test_MonteCarlo():
	""" Testing Monte Carlo functionality """
	from diffusion_model import energy	#use diffusion model energy function as test for functionality of MC minimisation
	import nose.tools
	from nose.tools import assert_equal
	from random import randint
	
	#minimum energy state doesn't change at absolute zero
	for n in range (10): #try ten times
		density=[1.0,1.0,1.0,1.0]
		MonteCarlo ("diffusion_model","energy",density)
		assert_equal(density,[1.0,1.0,1.0,1.0])
	
	#energy state lowers until minimum energy state is reached at absolute zero
	for n in range (10): #try ten times
		for i in range (10):
			density[i]=random.randint(1,10) #fill density with random integers
		if max(density)-min(density)<=1:
			density_backup=density[:]
			MonteCarlo("diffusion_model","energy",density)
			assert_true(density=density_backup)
		else:
			E0=energy(density)
			while (max(density)-min(density)>=2): #if distribution is non-uniform energy minimum is not reached
				MonteCarlo("diffusion_model","energy",density)
		assert_true(E0>=energy(density))