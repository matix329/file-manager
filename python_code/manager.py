import os
from file_operations import *
from mass_operations import *
from utilities import *

print("Input the command")

user_input = input()
while user_input != 'quit':
    if user_input[:3] == 'cd ':
        try:
            directory = user_input.split()[1]
            if directory == '..':
                os.chdir(os.path.dirname(os.getcwd()))
                print(os.getcwd().split('/')[-1])
            else:
                os.chdir(directory)
                print(os.getcwd().split('/')[-1])
        except (FileNotFoundError, IndexError):
            print("Invalid command")

    elif user_input == 'pwd':
        print(os.getcwd())

    elif user_input[:2] == 'ls':
        if user_input == 'ls':
            printing_directory(os.getcwd())
        else:
            printing_directory(os.getcwd(), argument=user_input.split()[1])

    elif user_input[:2] == 'rm':
        try:
            file_or_extension = user_input.split()[1]
            if file_or_extension.startswith('.') and len(file_or_extension) >= 2:
                files = [f for f in os.listdir() if os.path.isfile(f)]
                mass_rm(file_or_extension, files)
            else:
                remove_file_or_dir(file_or_extension)
        except IndexError:
            print("Specify the file or directory")

    elif user_input[:2] == 'mv':
        try:
            full_path = user_input.split()
            if full_path[1].startswith('.') and len(full_path[1]) > 1:
                extension = full_path[1]
                destination = full_path[2]
                files = [f for f in os.listdir() if os.path.isfile(f)]
                mass_mv(extension, files, destination)
            else:
                old_name, new_name = full_path[1], full_path[2]
                if not os.path.exists(old_name):
                    print("No such file or directory")
                else:
                    destination = new_name
                    if os.path.isdir(destination):
                        destination = os.path.join(destination, os.path.basename(old_name))
                    if os.path.exists(destination):
                        print("The file or directory already exists")
                    else:
                        shutil.move(old_name, destination)
                        print(f"'{old_name}' has been moved to '{destination}'")
        except IndexError:
            print("Specify the current name of the file or directory and the new location and/or name")

    elif user_input[:2] == 'cp':
        try:
            full_path = user_input.split()
            if len(full_path) == 1:
                print("Specify the file")
            elif full_path[1].startswith('.') and len(full_path[1]) > 1:
                extension = full_path[1]
                destination = full_path[2]
                files = [f for f in os.listdir() if os.path.isfile(f)]
                mass_cp(extension, files, destination)
            elif len(full_path) != 3:
                print("Specify the current name of the file or directory and the new location and/or name")
            else:
                source, destination = full_path[1], full_path[2]
                if not os.path.isabs(source):
                    source = os.path.abspath(source)
                if not os.path.isabs(destination):
                    destination = os.path.abspath(destination)
                if os.path.exists(source):
                    if not os.path.exists(os.path.join(destination, os.path.basename(source))):
                        shutil.copy(source, destination)
                        print(f"File '{os.path.basename(source)}' has been copied to '{destination}'")
                    else:
                        print(f"{os.path.basename(source)} already exists in this directory")
                else:
                    print("No such file or directory")
        except IndexError:
            print("Specify the file")

    elif user_input[:5] == 'mkdir':
        try:
            dir_name = user_input.split()[1]
            make_directory(dir_name)
        except IndexError:
            print("Specify the name of the directory to be made")

    else:
        print('Invalid command')

    user_input = input()
