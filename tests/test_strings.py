from unittest import TestCase
from strings import pyfullname
import ctypes


class TestStrings(TestCase):
    def test_pyfullname(self):
        first = ctypes.create_string_buffer(b"Joe")
        self.assertEqual(pyfullname(b"Joe", b"Doe").decode("UTF-8"), "Joe Doe")

        first = ctypes.create_string_buffer(b"Joe")  # Mutable data type
        last = ctypes.create_string_buffer(b"Done")
        self.assertEqual(pyfullname(first, last).decode("UTF-8"), "Joe Done")
