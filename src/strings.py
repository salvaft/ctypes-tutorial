import ctypes

clib = ctypes.CDLL("c_libs/build/strings.so")

pyfullname = clib.fullName

pyfullname.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
pyfullname.restype = ctypes.c_char_p

# print(pyfullname(b"John", b"Doe").decode("utf-8"))
# print(clib.fullName(b"John", b"Doe").decode("utf-8"))
