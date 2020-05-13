"""
This program moves all files of a given file type from one directory to another.

Author: John Jamora
Date Created: 10/05/2020
"""
import os
import shutil


def main():
    file_type = getType()
    origin = getOrigin()
    destination = getDestination()
    count = 0

    for file in os.listdir(origin):
        if file.endswith(file_type):
            move(file, origin, destination)
            count += 1
    print("Number of files moved:", count)


def getType():
    """
    Asks the user for the file type to be moved.

    Attributes:
        file_type: Name of the file extension

    :return: File Type
    """
    file_type = input("Which file format would you like to transfer?\n")
    confirmation = input(f"\"{file_type}\" selected, is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getType()
    return "." + file_type


def getOrigin():
    """
    Asks the user for the directory which the files are to be moved from.

    Attributes:
        origin: Name of the originating file directory

    :return: The originating file directory
    """
    origin = input("From which directory?\n")
    confirmation = input(f"Moving from \"{origin}\", is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getOrigin()
    return origin


def getDestination():
    """
    Asks the user for the directory which the files are to be moved to.

    Attributes:
        destination: Name of the terminus file directory.

    :return: The terminus file directory
    """
    destination = input("To which directory?\n")
    confirmation = input(f"Moving to \"{destination}\", is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getDestination()
    return destination


def move(file_name, origin, destination):
    """
    Moves a file from a specified directory to another.

    :param file_name: The file to be moved
    :param origin: The directory where the file is currently stored
    :param destination: The directory where the file is to be moved to

    :return: None
    """
    shutil.move(origin + "/" + file_name, destination)
    print(f"{file_name} was moved from {origin} to {destination}")


def searchDirectory(directory):
    """
    Searches through a specified directory and lists its children.

    :param directory: The directory to be searched
    :return: None
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))


if __name__ == "__main__":
    main()
