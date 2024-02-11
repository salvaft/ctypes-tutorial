import ctypes

clib = ctypes.CDLL("c_libs/build/argtypes.so")

pyadd = clib.add

pyadd.argtypes = [ctypes.c_int, ctypes.c_int]
pyadd.restype = ctypes.c_int

# print(pyadd(1, 2))
