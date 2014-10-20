from MCE import MonteCarlo
def test_MonteCarlo():
	""" Testing Monte Carlo functionality """
	#from diffusion_model import energy
	from nose.tools import assert_equal
	MonteCarlo ("diffusion_model","energy",[2.0, 1.0])
	
