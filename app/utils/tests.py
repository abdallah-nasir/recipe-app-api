from django.test import SimpleTestCase
from .calc import add_func


class UtilsTestCase(SimpleTestCase):
    """
    Test case for Calculation
    """

    def test_calc(self):
        res = add_func(nums=[5, 6])
        self.assertEqual(res, 11)
