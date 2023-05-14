import invoke
import pathlib
import sys
import os
import shutil
import glob
import platform


# Helper functions ==================================================

@invoke.task
def clean(c):
    """Remove any built objects"""
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd"
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    """Print a separating banner/title"""
    print("==================================================")
    print("= {} ".format(msg))


# Compile helper functions ==========================================

@invoke.task()
def build_mult(c):
    """Build the shared library for the sample C++ code"""
    print_banner("Building C++ Library")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC mult.cpp "
        "-o libmult.so "
    )
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    """Compile for the Python module and create bindings"""

    # If it's run on MacOS, add a flag to ignore missing symbols
    if platform.system() == "Darwin":
        linker_flags = "-undefined dynamic_lookup"
    else:
        linker_flags = ""

    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3 -m pybind11 --includes` "
        "-I . "
        "{0} "
        "-o {1}`python3-config --extension-suffix` "
        f"-L. -lmult -Wl,-rpath,. {linker_flags}".format(
            cpp_name, extension_name)
    )


# Build the wrapper and test ========================================

@invoke.task(build_mult)
def build_pybind11(c):
    """Build the pybind11 wrapper library"""
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_wrapper.cpp", "pybind11_toy")
    print("* Complete")


@invoke.task(build_pybind11)
def test_pybind11(c):
    """Run the script to test PyBind11"""
    print_banner("Testing PyBind11 Module")
    invoke.run("python3 pybind11_test.py", pty=True)


# Invoke all by calling all four functions ==========================

@invoke.task(
    clean,
    build_mult,
    build_pybind11,
    test_pybind11,
)
def all(c):
    """Build and run all tests"""
    pass

