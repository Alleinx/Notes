import unittest


class TestStringMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('This setup method will only be called once')

    @classmethod
    def tearDownClass(cls):
        print('This teardown method will only be called once')

    def setUp(self):
        print('setUp() method will be executed before every test method.')

    def tearDown(self):
        print('tearDown() method will be executed after every test method.')

    # Test method should start with 'test' prefix
    def test_upper(self):
        print('test_upper()')
        # check whether two things are equal
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # check conditions
        print('test_isupper()')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test_split()')

        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split() fails when the seperator is not a string

        # Use assertRaises() to check whether a specific type of exception is raised.
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    # start testing
    # unittest.main()

    # or you can customize your testing workflow
    # 1. define a suite
    suite = unittest.TestSuite()
    # 2. Add test method, the order of adding method is the execution order.
    suite.addTest(TestStringMethod('test_upper'))
    suite.addTest(TestStringMethod('test_split'))
    suite.addTest(TestStringMethod('test_isupper'))

    # 3. get a runner
    runner = unittest.TextTestRunner()
    # 4. perform test
    runner.run(suite)
