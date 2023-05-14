import os
import sys

# Add the 'build' directory to the module search path
build_dir = os.path.abspath('build')
sys.path.insert(0, build_dir)

# Import the module
import pybind11_toy

# Test the lib binding
if __name__ == "__main__":
    # Sample data for your call
    x, y = 6, 2.3

    answer = pybind11_toy.cpp_function(x, y)
    print(f"In the binded Python lib:")
    print(f" int - {x}")
    print(f" float - {y:.1f}")
    print(f" product - {answer:.1f}")
