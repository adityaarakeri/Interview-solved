import os

path = '/Users/aarakeri/PythonScripts/'

total_files = []


def print_dir_contents(path):
    global total_files

    for child in os.listdir(path):
        childpath = os.path.join(path, child)

        if os.path.isdir(childpath):
            print_dir_contents(childpath)
        else:
            print(childpath)
            total_files.append(childpath)


print_dir_contents(path)

print("\n Total files in the path {} : {}\n".format(path, len(total_files)))
