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
    file_type = input("Which file format would you like to transfer?\n")
    confirmation = input(f"\"{file_type}\" selected, is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getType()
    return "." + file_type


def getOrigin():
    origin = input("From which directory?\n")
    confirmation = input(f"Moving from \"{origin}\", is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getOrigin()
    return origin


def getDestination():
    destination = input("To which directory?\n")
    confirmation = input(f"Moving to \"{destination}\", is this correct? (Y/N)").lower()
    if confirmation not in {"y", "yes"}:
        getDestination()
    return destination


def move(filename, origin, destination):
    shutil.move(origin + "/" + filename, destination)
    print(f"{filename} was moved from {origin} to {destination}")


def searchDirectory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))


if __name__ == "__main__":
    main()
