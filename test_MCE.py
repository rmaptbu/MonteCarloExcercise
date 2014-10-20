from MCE import MonteCarlo
def test_MonteCarlo():
	""" Testing Monte Carlo functionality """
	from diffusion_model import energy
	import nose.tools
	from nose.tools import assert_equal
	assert_equal(MonteCarlo ("diffusion_model","energy",[4.0, 2.0, 5.0]),0)
	
