# This program demonstrate how to reuse your test code
# If you already have some testing method, and don't want to 
# move them into a TestCase.
# In this case, you can use unittest.FunctionTestCase(func, setUp, tearDown) -> TestCase
# to get a wrapped testCase, and use runner.run(testcase) to conduct testing.

import unittest

def test_someting():
    print('perform test_something()')
    assert [] is not None

if __name__ == "__main__":
    testcase = unittest.FunctionTestCase(test_someting, setUp=None, tearDown=None)
    runner = unittest.TextTestRunner()
    runner.run(testcase)