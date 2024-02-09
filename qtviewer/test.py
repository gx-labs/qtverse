import os
import mymodule
import sys

# CURRENT MODULE
# ----------------------------------------------------

# current module object
print(sys.modules[__name__])

# current module filepath
module_path = sys.modules[__name__].__file__
print(module_path)


# IMPORTED MODULE
# ----------------------------------------------------

# Imported module object
print(mymodule)

# Imported module filepath
print(mymodule.__file__)

# Imported module directory
module_dir = os.path.dirname(mymodule.__file__)
print(module_dir)
