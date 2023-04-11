import os


def get_files():

    if os.path.exists("directory/report.txt"): 
        os.remove("directory/report.txt")

    if os.path.exists("report.txt"):
        os.remove("report.txt")

    path = "directory"
    files = os.listdir(path)

    return files


def sort_files(files):


    extensions = set()
    for file_extension in files:
        extension = file_extension.split(".")[-1]
        extensions.add(f".{extension}")

    sorted_files = sorted(files)
    sorted_extensions = sorted(extensions)


    file1 = open("report.txt", "a+")
    file2 = open("directory/report.txt", "a+")


    for extension in sorted_extensions:
        file1.write(f"{extension}\n")
        file2.write(f"{extension}\n")

        for file in sorted_files:
            if extension in file:
                file1.write(f"- - - {file}\n")
                file2.write(f"- - - {file}\n")


    file1.close()
    file2.close()

    return "The result from the program is saved in report.txt"


files = get_files()
print(sort_files(files))