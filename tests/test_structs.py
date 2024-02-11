from unittest import TestCase
from structs import *
from typing import Type
import ctypes


class TestStructs(TestCase):
    def test_structs_to_c(self):
        my_point: Type[Point] = Point(5, 6)
        py_print_point(my_point)

    def test_structs_from_c(self):
        my_point: Type[Point] = py_create_point(5, 6)
        self.assertIsInstance(my_point, Point)
        self.assertEqual(my_point.x, 5)
        self.assertEqual(my_point.y, 6)

    def test_structs_pointer_from_c(self):
        my_point = py_create_point_pointer(5, 6)
        self.assertIsInstance(my_point, ctypes.POINTER(Point))
        print(my_point.contents)
        self.assertEqual(my_point.contents.x, 5)
        self.assertEqual(my_point.contents.y, 6)
        py_free_point(my_point)

    def test_structs_array_from_c(self):
        my_point_array = py_create_point_array(7)
        self.assertIsInstance(my_point_array, PointArray)
        self.assertEqual(my_point_array.size, 7)
        py_free_point_array(my_point_array)
