import os
import shutil

def mass_rm(extension, file_lst):
    is_there_ex = False
    for file in file_lst:
        if file.endswith(extension):
            is_there_ex = True
            os.remove(file)
            print(f"File '{file}' has been removed")
    if not is_there_ex:
        print(f"File extension {extension} not found in this directory")

def mass_cp(extension, file_lst, dst_path):
    is_there_ex = False
    if not os.path.exists(dst_path):
        print("No such file or directory")
        return

    for file in file_lst:
        if file.endswith(extension):
            is_there_ex = True
            dst_file_path = os.path.join(dst_path, file)
            if os.path.exists(dst_file_path):
                while True:
                    user_input = input(f"{file} already exists in this directory. Replace? (y/n): ").lower()
                    if user_input == 'y':
                        shutil.copy(file, dst_path)
                        print(f"File '{file}' has been copied to '{dst_path}'")
                        break
                    elif user_input == 'n':
                        break
                    else:
                        print("Please enter 'y' or 'n'")
            else:
                shutil.copy(file, dst_path)
                print(f"File '{file}' has been copied to '{dst_path}'")

    if not is_there_ex:
        print(f"File extension {extension} not found in this directory")

def mass_mv(extension, file_lst, dst_path):
    is_there_ex = False
    for file in file_lst:
        if file.endswith(extension):
            is_there_ex = True
            dst_file_path = os.path.join(dst_path, file)
            if os.path.exists(dst_file_path):
                while True:
                    user_input = input(f"{file} already exists in this directory. Replace? (y/n): ").lower()
                    if user_input == 'y':
                        shutil.copy(file, dst_path)
                        os.remove(file)
                        print(f"File '{file}' has been moved to '{dst_path}'")
                        break
                    elif user_input == 'n':
                        break
                    else:
                        print("Please enter 'y' or 'n'")
            else:
                shutil.move(file, dst_path)
                print(f"File '{file}' has been moved to '{dst_path}'")

    if not is_there_ex:
        print(f"File extension {extension} not found in this directory")
