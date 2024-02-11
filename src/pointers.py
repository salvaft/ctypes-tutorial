# Python cannot allocate nor deallocate memory using pointers
# At the same time, the pointer is not an entity in python
# To get over that ctypes offers a pointer datastructure
# and we will have to deallocate memory back in the C code

import ctypes

clib = ctypes.CDLL("c_libs/build/pointers.so")

full_name = clib.fullName
full_name.restype = ctypes.POINTER(ctypes.c_char_p)
full_name.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

free_full_name = clib.free_full_name
