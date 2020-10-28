'''
Write a function to search for a particular pattern of file in the 
current directory

'''


import os


def osWalkandFind(pat):

    pattern_lst = []

    for dirpath, dirname, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith(pat):
                pattern_lst.append(os.path.join(dirpath, filename))

    print("Files found of format({}): {}".format(pat, str(len(pattern_lst))))


osWalkandFind(input("\nEnter the pattern to search(ex: .txt, .py : "))
