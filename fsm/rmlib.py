"""Module to move and remove directories and files."""

import errno
import logging
import os
import sys

# Configure logging to output information and error messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def mv(src, dst):
    """
    Move a file from src to dst.

    Args:
        - src (str): Source path of the file.
        - dst (str): Destination path for the file.

    If a file already exists at the destination path, it logs an error.
    """
    try:
        os.rename(src, dst)
        logger.info("File by path %s was successfully moved.", src)
    except OSError as err:
        if err.errno == errno.EEXIST:
            logger.error("File already exists at the destination path.")
        else:
            sys.exit(err.strerror)


def mvdir(src, dst):
    """
    Move a directory from src to dst.

    Args:
        - src (str): Source path of the directory.
        - dst (str): Destination path for the directory.

    Moves all files within the source directory to the destination.
    """
    move_to = os.path.join(dst, os.path.basename(src))
    try:
        mkdir(move_to)  # ensure destination directory exists
        all_files = os.listdir(src)  # list all files in source directory
        for file in all_files:
            mv(os.path.join(src, file), os.path.join(move_to, file))  # move each file
        rmdir(src)  # remove source directory after moving files
        logger.info("Directory by path %s was successfully moved.", src)
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def rm(path):
    """
    Remove a file at the specified path.

    Args:
        - path (str): Path of the file to be removed.

    Logs an error if the file does not exist.
    """
    try:
        os.remove(path)
        logger.info("File by path %s was successfully removed.", path)
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def rmdir(path):
    """
    Remove a directory at the specified path.

    Args:
        - path (str): Path of the directory to be removed.

    Recursively removes all files and subdirectories.
    """
    try:
        if os.path.islink(path):
            os.unlink(path)
        if os.listdir(path):  # check if directory is not empty
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    rm(os.path.join(root, name))  # remove each file
                os.removedirs(root)  # remove directory
            logger.info("Directory by path %s was successfully removed.", path)
        else:
            os.removedirs(path)  # remove empty directory
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def mkdir(path):
    """
    Create a directory at the specified path.

    Args:
        - path (str): Path where the directory will be created.

    Logs an error if the directory already exists.
    """
    try:
        os.makedirs(path)
        logger.info("Directory by path %s was successfully created.", path)
    except OSError as err:
        if err.errno == errno.EEXIST:
            logger.error("Directory already exists at this path.")
        else:
            sys.exit(err.strerror)
