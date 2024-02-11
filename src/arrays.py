import ctypes


array = ctypes.c_int * 10


# for _, idx in enumerate(array()):
#     print(array[idx])


clib = ctypes.CDLL("c_libs/build/arrays.so")

py_sumArray = clib.sum_array

py_sumArray.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

py_sumArray.restype = ctypes.c_int


py_newArray = clib.new_array


class ArrayOfFive(ctypes.Structure):
    _fields_ = [("array", ctypes.c_int * 5)]


py_newArray.restype = ArrayOfFive

py_increment_array = clib.increment_array
py_increment_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
py_increment_array.restype = ctypes.POINTER(ctypes.c_int)
