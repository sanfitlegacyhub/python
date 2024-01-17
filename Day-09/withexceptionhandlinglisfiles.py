import os

def list_files_in_folder(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)

        # Display the list of files
        print("\nFiles in the folder:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied for folder '{folder_path}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Get the folder paths from the user
    input_paths = input("Enter multiple folder paths separated by commas: ")
    folder_paths = [path.strip() for path in input_paths.split(',')]

    # Call the function to list files in each folder
    for path in folder_paths:
        list_files_in_folder(path)

if __name__ == "__main__":
    main()
