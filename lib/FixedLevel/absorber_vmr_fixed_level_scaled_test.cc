#include "absorber_vmr_fixed_level_scaled.h"
#include "configuration_fixture.h"
#include "unit_test_support.h"

using namespace FullPhysics;
using namespace blitz;


BOOST_FIXTURE_TEST_SUITE(absorber_vmr_fixed_level_scaled, ConfigurationFixture)

BOOST_AUTO_TEST_CASE(basic)
{
  Array<double, 1> vmr(20);
  vmr = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20;
  double scale = 1.0;
  AbsorberVmrFixedLevelScaled avmr(config_pressure, 
				   config_pressure_level_input,
				   vmr, true, scale, "CO2");
  Array<double, 1> grid_expect(19);
  grid_expect = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18.3491376161;
  for(int i = 0; i < grid_expect.rows(); ++i)
    BOOST_CHECK_CLOSE(avmr.volume_mixing_ratio(config_pressure->pressure_grid()(i).value).value(), grid_expect(i), 1e-8);
}

BOOST_AUTO_TEST_SUITE_END()
