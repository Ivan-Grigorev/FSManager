"""Configuration for pytest fixtures."""

import os
import pytest


@pytest.fixture
def my_example(fs):
    """
    Fixture to set up an example file system structure for tests.

    Creates source and destination directories and a file for testing.
    Uses the 'pyfakefs' library for a fake file system in tests.

    Args:
        - fs: Fake file system object from pyfakefs.

    Returns:
        - tuple: (src, dst, file) paths for testing.
    """
    src = "src"  # source directory path
    dst = "dst"  # destination directory path
    file = "traveler.txt"  # file name to be used in tests

    fs.create_dir(src)  # create source directory
    fs.create_dir(dst)  # create destination directory
    fs.create_file(os.path.join(src, file))  # create a file in the source directory

    return src, dst, file  # return paths for testing
