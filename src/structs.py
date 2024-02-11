import ctypes


class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


clib = ctypes.CDLL("c_libs/build/structs.so")

py_print_point = clib.print_point
py_create_point = clib.create_point
py_create_point.argtypes = [ctypes.c_int, ctypes.c_int]
py_create_point.restype = Point


py_create_point_pointer = clib.create_point_pointer
py_create_point_pointer.argtypes = [ctypes.c_int, ctypes.c_int]
py_create_point_pointer.restype = ctypes.POINTER(Point)
py_free_point = clib.free_point

py_free_point = clib.free_point


class PointArray(ctypes.Structure):
    _fields_ = [("points", ctypes.POINTER(Point)), ("size", ctypes.c_int)]


py_create_point_array = clib.create_point_array
py_create_point_array.argtypes = [ctypes.c_int]
py_create_point_array.restype = PointArray
py_free_point_array = clib.free_point_array
