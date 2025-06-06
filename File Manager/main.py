import os

def create_file(filename):
    try:
        with open(filename, "w") as file:
            print(f"{filename} created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_file():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in current directory:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        edit = input("Enter what you want to add: ")
        with open(filename, "w") as file:
            file.write(edit)
        print("The file was updated successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("--- Welcome ---")
while True:
    print("\n1. Create File")
    print("2. View All Files")
    print("3. Delete File")
    print("4. Edit File")
    print("5. Exit")
    try:
        user = int(input("What do you want to do (1–5): "))
        if user == 1:
            filename = input("Enter the name of the file: ")
            create_file(filename)
        elif user == 2:
            view_file()
        elif user == 3:
            filename = input("Enter the name of the file to delete: ")
            delete_file(filename)
        elif user == 4:
            filename = input("Enter the name of the file to edit: ")
            edit_file(filename)
        elif user == 5:
            print("Exiting program...")
            break
        else:
            print("Please enter a valid option.")
    except ValueError:
        print("Please enter a number.")