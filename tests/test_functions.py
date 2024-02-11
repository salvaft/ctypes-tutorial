from unittest import TestCase
from functions.argtypes import pyadd
from functions.hello_world import pyhelloworld


class TestStrings(TestCase):
    def test_pyadd(self):
        self.assertEqual(pyadd(2, 3), 5)
        self.assertEqual(pyadd(0, 0), 0)
        self.assertEqual(pyadd(-1, 0), -1)
        self.assertEqual(pyadd(-1, -1), -2)

    def test_pyhelloworld(self):
        self.assertIsNotNone(pyhelloworld())
