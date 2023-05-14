# Python bindings for C++: pybind11 + invoke

## What is invoke?

Invoke is a Python-based task execution tool that allows developers to define and run tasks in a simple, readable format. It provides a high-level API to run shell commands. We could create CLI-invokable tasks by defining/organizing task functions from a `tasks.py` file. It performs a similar role to make but uses Python instead of Makefiles.

## Why invoke?
When it comes to creating Python bindings for C++ code, both `cmake` and `invoke` can be used. However, the choice between the two depends on the specific requirements of your project. Here are some advantages of using `invoke` for Python bindings:

1. Simplicity: `invoke` is a simpler tool compared to `cmake`. If your project is relatively small and does not have complex build requirements, `invoke` might be a better choice.
2. Pythonic: `invoke` is a Pythonic tool and is designed to work seamlessly with Python projects. If your project is primarily written in Python, `invoke` might be a better choice.
3. Flexibility: `invoke` provides more flexibility compared to `cmake`. It allows you to define and execute tasks in Python, which gives you more control over the build process.
4. Familiarity: If you are already familiar with Python and its ecosystem, using `invoke` for Python bindings might be a more natural choice.

## About this repo

This is a toy example showing how to create Python bindings to interface with a C++ library using invoke.

## Environment
It runs on Linux and MacOS.


## Create and activate a python virtual environment
```
./1.setup.sh
source env/bin/activate
./2.install.sh
```

## Check the available invoke tasks.

```
invoke --list
```

## Test the bindings.
```
invoke test-pybind11
```
You should see the output as below.
```
==================================================
= Building C++ Library
* Complete
==================================================
= Building PyBind11 Module
* Complete
==================================================
= Testing PyBind11 Module
In the C++ function:
int - 6
float - 2.3
product - 13.8
In the binded Python lib:
int - 6
float - 2.3
product - 13.8
```
You can edit the `test_pybind11` in `tasks.py` for your own tests.
