# Error Handling Lab 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print("\nFile content:\n")
        print(data)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except PermissionError:
    print("You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
