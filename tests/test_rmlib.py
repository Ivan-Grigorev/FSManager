"""Module to test functions from rmlib.py."""

import os

from fsm.rmlib import mkdir, mv, mvdir, rm, rmdir


def test_mv(my_example):
    """
    Tests the mv() function for moving files.

    Moves a file from the source directory to the destination directory
    and verifies the move was successful.
    """
    move_from = os.path.join(my_example[0], my_example[2])  # source file path
    move_to = os.path.join(my_example[1], my_example[2])  # destination file path
    mv(move_from, move_to)

    assert os.path.exists(move_from) == False  # check file is moved from source
    assert os.path.exists(move_to) == True  # check file exists at destination


def test_mvdir(my_example):
    """
    Tests the mvdir() function for moving directories.

    Moves a directory from the source to the destination and verifies
    the directory and its contents were successfully moved.
    """
    src_files = len(os.listdir(my_example[0]))  # number of files in source
    src_folder = os.path.basename(my_example[0])  # source folder name
    mvdir(my_example[0], my_example[1])

    assert os.path.exists(my_example[0]) == False  # check source dir is moved
    assert os.path.exists(os.path.join(my_example[1], src_folder)) == True  # check destination dir exists
    assert src_files == len(os.listdir(os.path.join(my_example[1], src_folder)))  # verify file count


def test_rm(my_example):
    """
    Tests the rm() function for removing files.

    Removes a file and verifies it no longer exists.
    """
    file_path = os.path.join(my_example[0], my_example[2])  # file to be removed
    rm(file_path)

    assert os.path.exists(file_path) == False  # check file is removed


def test_rmdir(my_example):
    """
    Tests the rmdir() function for removing directories.

    Removes a directory and verifies it no longer exists.
    """
    rmdir(my_example[0])

    assert os.path.exists(my_example[0]) == False  # check directory is removed


def test_mkdir(my_example):
    """
    Tests the mkdir() function for creating directories.

    Creates a directory and verifies it exists.
    """
    new_dir = os.path.join(my_example[1], "new_dir")  # directory to be created
    mkdir(new_dir)

    assert os.path.exists(new_dir) == True  # check directory is created
