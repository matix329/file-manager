import os
import shutil

def remove_file_or_dir(path):
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                print(f"File '{path}' has been removed")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Directory '{path}' has been removed")
        else:
            print("No such file or directory")
    except FileNotFoundError:
        print("No such file or directory")
    except shutil.Error as e:
        print(f"Error occurred while deleting: {e}")

def rename_file_or_dir(old_name, new_name):
    try:
        if not os.path.isabs(new_name):
            new_name = os.path.abspath(new_name)

        if os.path.exists(old_name):
            if not os.path.exists(new_name):
                shutil.move(old_name, new_name)
                print(f"'{old_name}' has been moved to '{new_name}'")
            else:
                print("The file or directory already exists")
        else:
            print("No such file or directory")
    except FileExistsError:
        print("The file or directory already exists")
    except FileNotFoundError:
        print("No such file or directory")

def copy_file(source, destination):
    try:
        if not os.path.isabs(destination):
            destination = os.path.abspath(destination)

        if os.path.exists(source):
            if not os.path.exists(destination):
                shutil.copy(source, destination)
                print(f"File '{source}' has been copied to '{destination}'")
            else:
                print(f"'{os.path.basename(destination)}' already exists in this directory")
        else:
            print("No such file or directory")
    except FileExistsError:
        print(f"'{os.path.basename(destination)}' already exists in this directory")
    except FileNotFoundError:
        print("No such file or directory")

def make_directory(dir_name):
    try:
        if len(dir_name) > 0 and not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(f"Directory '{dir_name}' has been created")
        else:
            print("The directory already exists")
    except FileExistsError:
        print("The directory already exists")
    except FileNotFoundError:
        print("No such file or directory")
