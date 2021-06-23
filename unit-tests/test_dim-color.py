import unittest
import dim_color

class TestDim(unittest.TestCase):

    def test_dim_color(self):
        self.assertEqual(dim_color.dim_color("000"), "000")
        self.assertEqual(dim_color.dim_color("#000"), "#000")
        self.assertEqual(dim_color.dim_color("000000"), "000000")
        self.assertEqual(dim_color.dim_color("#000000"), "#000000")
        self.assertEqual(dim_color.dim_color("000"), "000")
    
    def test_check_argv(self):
        self.assertEqual(dim_color.check_argv([dim_color.__file__, "#"]), (False, dim_color.INVALID_VALUE_MSG))
        self.assertEqual(dim_color.check_argv([dim_color.__file__, "#123"]), (True, "#123"))
        self.assertEqual(dim_color.check_argv([dim_color.__file__, "#0001233"]), (False, dim_color.INVALID_VALUE_MSG))
        self.assertEqual(dim_color.check_argv([dim_color.__file__, "#000123"]), (True, "#000123"))
        self.assertEqual(dim_color.check_argv([dim_color.__file__]), (False, dim_color.INVALID_ARGS_MSG))

if __name__ == "__main__":
    # allows test to run directly from script
    unittest.main()
