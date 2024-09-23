import os

def converting_bytes(filesize):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    size_suffix = 0
    while filesize // 1024 > 0:
        filesize /= 1024
        size_suffix += 1
    return f'{int(filesize)}{suffixes[size_suffix]}'

def printing_directory(directory, argument=None):
    directories = []
    files = []

    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_dir():
                directories.append(entry.name)
            elif entry.is_file():
                files.append(entry.name)

    directories.sort()
    files.sort()

    if len(directories) > 0:
        print(*directories, sep='\n')

    if len(files) > 0:
        print(*files, sep='\n')
