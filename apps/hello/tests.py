from django.test import TestCase

# Create your tests here.

class SomeTests(TestCase):
    def test_math(self):
        '''testing 2+2'''
        self.assertEqual(2+2, 4)
