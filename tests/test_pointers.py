from unittest import TestCase
from pointers import full_name, free_full_name
import ctypes


class TestPointers(TestCase):
    def test_allocating(self):
        ptr = full_name(b"John", b"Doe")

        cstring = ctypes.c_char_p.from_buffer(ptr)
        self.assertEqual(cstring.value.decode("UTF-8"), "John Doe")

        free_full_name(ptr)
        with self.assertRaises(UnicodeDecodeError):
            cstring.value.decode("UTF-8")  # Garbage value

    def test_pointers_contents(self):
        num = ctypes.c_int(5)
        ptr = ctypes.pointer(
            num
        )  # Gets the reference to the variable. It needs an instance of  ctypes data type

        self.assertEqual(ptr.contents.value, 5)

        ptr2 = ctypes.POINTER(
            ctypes.c_int
        )  # This is a class in the ctypes module. It is used to create a pointer type. You use it as a type specifier when defining the argument types of functions or when creating arrays of pointers.
        ptr2.contents = num
        self.assertEqual(ptr2.contents.value, 5)

        # ctypes.POINTER is a class used to define pointer types for use in function signatures or array declarations.
