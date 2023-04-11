import os
import time


def create_file(file_name, *args): 
    try:
        ''' Delete file content '''

        os.remove(file_name)
        file = open(file_name, "x")
        file.close()
        print(f"File {file_name} content was deleted")

    except FileNotFoundError:
        ''' Create file '''

        file = open(file_name, "x")
        file.close()
        print(f"File {file_name} was created")


def add_content(file_name, *args_content):
    content = args_content[0]

    if os.path.exists(file_name):
        print(f"Content added to {file_name}")

    else:
        print(f"Created {file_name} and added content")

    file = open(file_name, "a+")
    file.write(f"{content}\n")
    file.close()


def replace_content(file_name, *content):
    old_content, new_content, = content[0], content[1]

    try:

        file = open(file_name, "r")
        lines = [line for line in file]
        file.close()

        for index, line in enumerate(lines):
            line = line.replace(old_content, new_content)
            lines[index] = line

        os.remove(file_name)
        file = open(file_name, "x")
        file.close()

        file = open(file_name, "a+")
        [file.write(line) for line in lines]
        file.close()

        print(f"{file_name}'s content successfully changed")

    except FileNotFoundError:
        print("An error occurred", "# replacing content")


def delete_file(file_name, *args):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File {file_name} was removed")
    else:
        print("An error occurred", "# Cannot delete file that does not exist")


operations = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file
}

command = input()
while command != "End":

    operation, name_of_file, *more_content = command.split("-")

    operations[operation](name_of_file, *more_content)

    time.sleep(0.1)

    command = input()
