import unittest

def get_formatted_name(first, last, middle =''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
        
    return full_name.title()

# Test class should extend from "unittest.TestCase"
class NameTestCase(unittest.TestCase):

    # name of a test method should start with 'test', otherwise, python won't execute
    # it.
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        # use assert here
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == "__main__":
    unittest.main()