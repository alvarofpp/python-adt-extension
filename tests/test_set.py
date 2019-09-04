import unittest
from adt_extension import Set


class SwitchDictTest(unittest.TestCase):
    def test_add_int_even(self):
        """Check add() for even integers."""
        # Set
        set_int_even = Set(element_type=int, rule=lambda x: (x % 2 == 0))
        # Elements that satisfies the element type and validation rule
        set_int_even.add(4)
        set_int_even.add(6)
        # Elements that satisfies the element type, but not validation rule
        set_int_even.add(5)
        # Elements that not satisfies the element type
        set_int_even.add("qwe")
        set_int_even.add(True)

        self.assertTrue(len(set_int_even) == 2)

    def test_add_odd(self):
        """Check add() for odd numbers."""
        # Set
        set_odd = Set(rule=lambda x: (x % 2 == 1))
        # Elements that satisfies the validation rule
        set_odd.add(3.)
        set_odd.add(5)
        set_odd.add(7)
        # Elements that not satisfies the validation rule
        set_odd.add(2.)
        set_odd.add(4)

        self.assertTrue(len(set_odd) == 3)

    def test_add_float(self):
        """Check add() for floating numbers."""
        # Set
        set_float = Set(element_type=float)
        # Elements that satisfies the element type
        set_float.add(7.)
        set_float.add(8.)
        set_float.add(9.)
        # Elements that not satisfies the element type
        set_float.add("asd")
        set_float.add(False)
        set_float.add(10)

        self.assertTrue(len(set_float) == 3)

    def test_update_int_even(self):
        """Check update() for even integers."""
        # Set
        set_int_even = Set(element_type=int, rule=lambda x: (x % 2 == 0))
        # Elements that satisfies the element type and validation rule
        set_int_even.update({4, 6})
        # Elements that satisfies the element type, but not validation rule
        set_int_even.update({5})
        # Elements that not satisfies the element type
        set_int_even.update({"qwe", True})

        self.assertTrue(len(set_int_even) == 2)

    def test_update_odd(self):
        """Check update() for odd numbers."""
        # Set
        set_odd = Set(rule=lambda x: (x % 2 == 1))
        # Elements that satisfies the validation rule
        set_odd.update({3., 5, 7})
        # Elements that not satisfies the validation rule
        set_odd.update({2., 4})

        self.assertTrue(len(set_odd) == 3)

    def test_update_float(self):
        """Check update() for floating numbers."""
        # Set
        set_float = Set(element_type=float)
        # Elements that satisfies the element type
        set_float.update({7., 8., 9.})
        # Elements that not satisfies the element type
        set_float.update({"asd", False, 10})

        self.assertTrue(len(set_float) == 3)
