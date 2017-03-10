import pathlib
import unittest

import pkg_resources as pkgr

from ideal_octo_parakeet import Grib

class Test(unittest.TestCase):

    def setUp(self):
        path = pathlib.Path('data', 'ds.sky.bin')
        self.ndfd_sky = pkgr.resource_filename(__name__, str(path))

    def test_sky(self):
        gf = Grib(self.ndfd_sky)
        s = str(gf)
        expected = ("MsgNum, Byte, GRIB-Version, elem, level, reference(UTC), valid(UTC), Proj(hr)"
            '1.0, 0, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 00:00, 3.00'
            '2.0, 285, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 03:00, 6.00'
            '3.0, 530, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 06:00, 9.00'
            '4.0, 775, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 09:00, 12.00'
            '5.0, 1020, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 12:00, 15.00'
            '6.0, 1265, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 15:00, 18.00'
            '7.0, 1510, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 18:00, 21.00'
            '8.0, 1755, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/11/2017 21:00, 24.00'
            '9.0, 2000, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 00:00, 27.00'
            '10.0, 2245, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 03:00, 30.00'
            '11.0, 2490, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 06:00, 33.00'
            '12.0, 2735, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 09:00, 36.00'
            '13.0, 2980, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 12:00, 39.00'
            '14.0, 3225, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 15:00, 42.00'
            '15.0, 3470, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 18:00, 45.00'
            '16.0, 3715, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/12/2017 21:00, 48.00'
            '17.0, 3960, 2, Sky="Total cloud cover [%]", 0-SFC, 03/10/2017 21:00, 03/13/2017 00:00, 51.00'
        )

        self.assertEqual(s, expected)
