def test_python_environment():
    import sys
    REQUIRED_PYTHON = "{{ cookiecutter.python_interpreter }}"
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
        assert system_major > required_major
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
        assert system_major > required_major
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")
