import numpy as np

# WRONG: ValueError when traits is a Python list (not a numpy array)
# NumPy array constructors typically accept nested sequences, but many
# other numpy functions are stricter. This demo creates a numpy.dtype
# object with a list of field descriptions, which triggers a TypeError.
try:
    dtype_obj = np.dtype([('f8', float), ('i4', int)])
    print("dtype created with fields:", dtype_obj.names)
except TypeError as e:
    print("Expected error:", type(e).__name__, str(e)[:120])
