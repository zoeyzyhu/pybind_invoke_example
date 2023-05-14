import pybind11_toy

if __name__ == "__main__":
    # Sample data for your call
    x, y = 6, 2.3

    answer = pybind11_toy.cpp_function(x, y)
    print(f"In the binded Python lib:")
    print(f" int - {x}")
    print(f" float - {y:.1f}")
    print(f" product - {answer:.1f}")
