"""Script to run file and directory operations using rmlib.py"""

from fsm.rmlib import mkdir, mv, mvdir, rm, rmdir


def main():
    """
    Main function to perform file and directory operations.

    It moves a file, moves a directory, removes a file, removes a directory,
    and creates a new directory.
    """
    # Move a file from source to destination
    mv(
        "/path/to/directory/src/traveler.txt",
        "/path/to/directory/dst/traveler.txt",
    )

    # Move a directory from source to destination
    mvdir("/path/to/directory/src", "/path/to/directory/dst")

    # Remove a file
    rm("/path/to/directory/src/traveler.txt")

    # Remove a directory
    rmdir("/path/to/directory/src")

    # Create a new directory
    mkdir("/path/to/directory/new/")


if __name__ == "__main__":
    main()
