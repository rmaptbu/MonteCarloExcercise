from MCE import MonteCarlo
def test_MonteCarlo():
	""" Testing Monte Carlo functionality """
	from diffusion_model import energy	#use diffusion model energy function as test for functionality of MC minimisation
	import nose.tools
	from nose.tools import assert_equal
	density=[1.0,1.0,1.0,1.0]
	MonteCarlo ("diffusion_model","energy",density)
	assert_equal(density,[1.0,1.0,1.0,1.0])
	
