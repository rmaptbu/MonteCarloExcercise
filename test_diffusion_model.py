from diffusion_model import energy
def test_energy():
  """ Optional description for nose reporting """
  # Test something
  
  from nose.tools import assert_equal
  assert_equal(energy([0.0,0.0],1.0), 0)