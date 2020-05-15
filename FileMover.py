"""
This program moves all files of a given file type from one directory to another.

Author: John Jamora
Date Created: 10/05/2020
"""
import os
import shutil


def main():
    options = {
        2: move
    }
    options[menu()]()


def menu():
    """
    Generates a menu of all the functions of this program.

    :return: The desired function to run.
    """

    options = ["Move a single file", "Move multiple files"]
    while True:
        print("What would you like do to?")
        for i, option in enumerate(options):
            print(str(i + 1) + ". " + option)
        action = int(input())
        if action in {1, 2}:
            print(f"You selected {options[action - 1].lower()}, is this correct? (Y|N)")
            proceed = input().lower()
            if proceed in {"y", "yes"}:
                return action
        else:
            print("Invalid entry. Please select a number from the menu.")
    

def move():
    """
    Moves files from one directory to another

    :return: None
    """

    file_type = getType()
    while True:
        try:
            origin = getOrigin()
            if not os.path.isdir(origin):
                raise FileNotFoundError
            break
        except FileNotFoundError:
            print(f"The system cannot find the path specified: \"{origin}\". Please try again.")

    while True:
        try:
            destination = getDestination()
            if not os.path.isdir(destination):
                raise FileNotFoundError
            break
        except FileNotFoundError:
            print(f"The system cannot find the path specified: \"{destination}\"")

    count = 0

    for file in os.listdir(origin):
        if file.endswith(file_type):
            moveFile(file, origin, destination)
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
    return file_type if file_type[0] == "." else "." + file_type


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


def moveFile(file_name, origin, destination):
    """
    Moves a single file from a specified directory to another.

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
