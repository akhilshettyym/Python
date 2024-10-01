# Write a python program to print the contents of a directory using the os module. Search online for the function which does that. a simple program
    
    
import os

# Function to print the contents of a directory
def print_directory_contents(path):
    try:
        # Get the list of files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")

# Example directory path (current directory)
directory_path = '.'
print_directory_contents(directory_path)
