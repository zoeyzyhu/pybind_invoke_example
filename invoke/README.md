# Python bindings for C++: pybind11 + invoke

This is a toy example showing how to create Python bindings to interface with a C++ library using invoke.

-   **Environment**: it runs on Linux and MacOS.
-   **How to use it**:

    -   Create a python virtual environment and activate it.

        ```
        python3 -m venv env
        source env/bin/activate
        ```

    -   Upgrade the Python tools in your virtual environment.

        ```
        pip install --upgrade pip setuptools
        ```

    -   Install the dependencies and double confirm.

        ```
        pip install -r requirements.txt
        pip list
        ```

    -   Check the available invoke tasks.

        ```
        invoke --list
        ```

    -   Test the bindings.

        ```
        invoke test-pybind11
        ```

    -   You should see the output as below.

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

    -   Edit the `test_pybind11` in `tasks.py` for your own tests.
