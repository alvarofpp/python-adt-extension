import unittest
from adt_extension import SwitchDict


class SwitchDictTest(unittest.TestCase):
    def setUp(self):
        """New object for all tests."""
        self.switch_dict = SwitchDict({
            'test1': 1,
            'test2': 2,
            'test3': 3,
        })

    def test_overload_getitem(self):
        """Check default case."""
        self.switch_dict.default_case = 'Default case here'
        # Exist index
        self.assertEqual(self.switch_dict['test1'], 1)
        # Default case
        self.assertEqual(self.switch_dict.default_case, 'Default case here')
        # Not exist index
        test_value = self.switch_dict['testtest']
        self.assertEqual(test_value, 'Default case here')
        # Not exist index and not exist default_case
        self.switch_dict.default_case = None
        with self.assertRaises(KeyError) as raises:
            test_value = self.switch_dict['testest']
