# This program demonstrate how to skip test

import sys
import unittest


class MyTestCase(unittest.TestCase):

    @unittest.skip('Demonstrating skipping')
    def test_nothing(self):
        # fail(msg), fail immediately.
        self.fail('shouldn\'t happen')

    @unittest.skipIf(sys.version < '1.1', 'not supported in this lib version')
    def test_format(self):
        # Tests that work for only a certain version of the lib.
        pass

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires windows')
    def test_windows_support(self):
        # windows specific testing code
        pass

    @unittest.expectedFailure
    def test_maybe_skipped(self):
        # use self.skipTest() to skip this test
        self.skipTest('External resource not available')
        # test code that depends on the external resource
        pass


@unittest.skip('Skip this TestCase class')
class SkipTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('LOO', 'loo'.upper())


if __name__ == "__main__":
    unittest.main()
