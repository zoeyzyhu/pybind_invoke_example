#include <pybind11/pybind11.h>
#include "mult.h"

PYBIND11_MODULE(pybind11_toy, module) {
    module.doc() = "pybind11 toy example"; // Optional
    module.def("cpp_function", &mult, 
		    "A function multiplying two numbers");
}
