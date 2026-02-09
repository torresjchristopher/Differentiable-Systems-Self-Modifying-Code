import unittest

class TestAutoDiff(unittest.TestCase):

    def setUp(self):
        # Initialize the automatic differentiation system here
        self.autodiff_system = None  # Replace with actual initialization

    def test_simple_function(self):
        x = 2.0
        expected_derivative = 1.0  # Replace with expected value
        self.assertAlmostEqual(self.autodiff_system.derivative(lambda x: x**2, x), expected_derivative)

    def test_composite_function(self):
        x = 3.0
        expected_derivative = 2 * 3.0  # Replace with expected value
        self.assertAlmostEqual(self.autodiff_system.derivative(lambda x: x**2 + 3*x, x), expected_derivative)

    def test_trigonometric_function(self):
        x = 0.0
        expected_derivative = 1.0  # Replace with expected value
        self.assertAlmostEqual(self.autodiff_system.derivative(lambda x: math.sin(x), x), expected_derivative)

if __name__ == '__main__':
    unittest.main()