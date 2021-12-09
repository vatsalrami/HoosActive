from django.test import TestCase
# Create your tests here.
class DummyTestCase(TestCase):
    def test_dummy(self):
        expected = 2
        actual = 1 + 1
        self.assertEqual(actual, expected)