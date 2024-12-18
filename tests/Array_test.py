import unittest
import utils.convert_array_to_desmos
class Array_Test(unittest.TestCase):
    def test_repeats_and_floats(self):
        assert utils.convert_array_to_desmos.convert_array_to_desmos_list([1,9.99,1]) == r"\left[1, 9.99, 1\right]", r"Should be \left[1, 9.99, 1\right]"
    

if __name__ == '__main__':
    unittest.main()