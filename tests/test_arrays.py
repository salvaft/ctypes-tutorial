from unittest import TestCase
from typing import Type
import ctypes
from arrays import py_sumArray, py_newArray, ArrayOfFive, py_increment_array


class TestArray(TestCase):
    def test_sum_array(self):
        array = ctypes.c_int * 5
        arr = array(1, 2, 3, 4, 5)
        self.assertEqual(py_sumArray(arr, 5), 15)

    def test_new_array(self):
        arr: Type[ArrayOfFive] = py_newArray()
        arr2: Type[ArrayOfFive] = py_newArray()
        self.assertListEqual(list(arr.array), list(arr2.array))

    def test_increment_array(self):
        array = ctypes.c_int * 5
        arr = array(1, 2, 3, 4, 5)
        res_ptr = py_increment_array(arr, 5)

        c_int_array = ctypes.cast(res_ptr, ctypes.POINTER(ctypes.c_int * 5)).contents

        self.assertListEqual(list(c_int_array), [2, 3, 4, 5, 6])
