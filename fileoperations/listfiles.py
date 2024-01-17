import os

def list_directory_contents(directory_path='.'):
    try:
        # Get the list of files and directories in the specified path
        contents = os.listdir(directory_path)
        
        print(f"Contents of directory '{directory_path}':")
        
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get the directory path from user input (default is the current directory)
directory_path = input("Enter the path of the directory (press Enter for current directory): ")

# List directory contents
list_directory_contents(directory_path)