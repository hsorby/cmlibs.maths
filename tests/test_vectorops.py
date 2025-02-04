import unittest
from math import sqrt

from cmlibs.maths.vectorops import distance, distance_squared, magnitude, magnitude_squared


class VectorOpsTestCase(unittest.TestCase):

    def test_magnitude(self):
        v = [1.0, 2.0, -3.0]
        expected_magnitude_squared = 14.0
        expected_magnitude = sqrt(expected_magnitude_squared)

        TOL = 1.0E-14
        self.assertAlmostEqual(magnitude(v), expected_magnitude, delta=TOL)
        self.assertAlmostEqual(magnitude_squared(v), expected_magnitude_squared, delta=TOL)

    def test_distance(self):
        u = [0.5, -0.1, 0.8]
        v = [1.5, -2.1, 3.8]
        expected_distance_squared = 14.0
        expected_distance = sqrt(expected_distance_squared)

        TOL = 1.0E-14
        self.assertAlmostEqual(distance(u, v), expected_distance, delta=TOL)
        self.assertAlmostEqual(distance_squared(u, v), expected_distance_squared, delta=TOL)


if __name__ == "__main__":
    unittest.main()
