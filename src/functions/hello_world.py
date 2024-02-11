import ctypes

clib = ctypes.CDLL("c_libs/build/hello_world.so")

pyhelloworld = clib.hello_world
