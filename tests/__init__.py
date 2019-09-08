import unittest

import tests.test_set
import tests.test_switchdict


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(tests.test_set))
    suite.addTests(loader.loadTestsFromModule(tests.test_switchdict))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())