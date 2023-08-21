import Lib_complex as lc
import unittest
import math

class Test_operatios_complex(unittest.TestCase):

    def test_sum(self):
        sum = lc.sum_complex((3, 5), (-2.6, 6.8))
        self.assertAlmostEqual(sum[0], 0.4)
        self.assertAlmostEqual(sum[1], 11.8)

    def test_sum2(self):
        sum = lc.sum_complex((3,2),(-5,5.2))
        self.assertAlmostEqual(sum[0], -2)
        self.assertAlmostEqual(sum[1], 7.2)

    def test_rest(self):
        rest = lc.rest_complex((3,2),(-5,5.2))
        self.assertAlmostEqual(rest[0], 8)
        self.assertAlmostEqual(rest[1], -3.2)

    def test_rest2(self):
        rest = lc.rest_complex((9,5),(-5,5.2))
        self.assertAlmostEqual(rest[0], 14)
        self.assertAlmostEqual(rest[1], -0.2)

    def test_mult(self):
        mult = lc.mult_complex((3,2),(-5,5.2))
        self.assertAlmostEqual(mult[0], -25.4)
        self.assertAlmostEqual(mult[1], 5.6)

    def test_mult2(self):
        mult = lc.mult_complex((9,5),(-5,5.2))
        self.assertAlmostEqual(mult[0], -71)
        self.assertAlmostEqual(mult[1], -21.8)

    def test_div(self):
        div = lc.div_complex((3,2),(-5,5.2))
        self.assertAlmostEqual(div[0], -0.08839354342813219)
        self.assertAlmostEqual(div[1], -0.49192928516525747)

    def test_div2(self):
        div = lc.div_complex((9,5),(-5,5.2))
        self.assertAlmostEqual(div[0], -0.3651037663335895)
        self.assertAlmostEqual(div[1], -1.3797079169869333)

    def test_div(self):
        div = lc.div_complex((3,2),(-5,5.2))
        self.assertAlmostEqual(div[0], -0.08839354342813219)
        self.assertAlmostEqual(div[1], -0.49192928516525747)

    def test_div2(self):
        div = lc.div_complex((9,5),(-5,5.2))
        self.assertAlmostEqual(div[0], -0.3651037663335895)
        self.assertAlmostEqual(div[1], -1.3797079169869333)

    def test_mod(self):
        self.assertAlmostEqual(lc.mod_complex((3,2)), 3.605551275463989)

    def test_mod2(self):
        self.assertAlmostEqual(lc.mod_complex((9, 5)), 10.295630140987)

    def test_conj(self):
        self.assertAlmostEqual(lc.conj_complex((3,2)), (3,-2))

    def test_conj2(self):
        self.assertAlmostEqual(lc.conj_complex((9, 5)), (9, -5))

    def test_car_pol(self):
        pol = lc.car_pol_complex((3,2))
        self.assertAlmostEqual(pol[0],3.605551275463989)
        self.assertAlmostEqual(pol[1],0.5880026035475675)

    def test_car_pol2(self):
        pol = lc.car_pol_complex((9, 5))
        self.assertAlmostEqual(pol[0], 10.295630140987)
        self.assertAlmostEqual(pol[1], 0.507098504392337)

    def test_pol_car(self):
        car = lc.pol_car_complex((3,math.pi/6))
        self.assertAlmostEqual(car[0],2.598076211353316)
        self.assertAlmostEqual(car[1],1.5)

    def test_car_pol2(self):
        car = lc.pol_car_complex((9, math.pi/3 ))
        self.assertAlmostEqual(car[0], 4.5)
        self.assertAlmostEqual(car[1], 7.794228634059947)

    def test_fase(self):
        self.assertAlmostEqual(lc.fase_complex((3, 2)), 0.5880026035475675)

    def test_fase2(self):
        self.assertAlmostEqual(lc.fase_complex((9, 5)), 0.507098504392337)

if __name__ == '__main__':
    unittest.main()


