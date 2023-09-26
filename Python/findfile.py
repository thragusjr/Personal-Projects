# findfile: a program that compares and contrasts user provided systems to identify if 
# target files are present on a single system, both systems, or neither sytem.
# author: Ethan Page
# version: 9/26/23

import os


def findfile():
    # declarations of keys used to match file names
    # made so users do not have to type exact filename (i.e. pallas as opposed to pallas.list)
    key1: str = input('Please enter the filename for the first system')
    key2: str = input('Please enter the filename for the second system')

    # declaration of search prefix variable
    prefix = input('Please enter the prefix to test')

    # declaration of variables used to match keys with actual file names
    system1: str = 'pallas.list'
    system2: str = 'minerva.list'
    system3: str = 'athena.list'

    # these can also be taken in by user if preferred
    pallasDir = "C:\Users\Documents\pallas.list"
    minervaDir = "C:\Users\Documents\minerva.list"
    athenaDir = "C:\Users\Documents\athena.list"

    # opening and reading files based on whether keys (search prefixes) match the file names
    # locate correct first file based on key
    # TODO correct misspelled class name (ITT383->ITT385)
    if key1 in system1:
        with open(pallasDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file1 = f.readlines()

    if key1 in system2:
        with open(minervaDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file1 = f.readlines()

    if key1 in system3:
        with open(athenaDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file1 = f.readlines()

    # file list declarations - used to build lists from file contents
    file_list1 = []
    file_list2 = []

    # match list declarations - used to build lists from search matches
    return_list1 = []
    return_list2 = []

    # declarations for the complete file name of matches
    file1_loc = ''
    file2_loc = ''

    # build list from first system file
    for i in file1:
        file_list1.append(i)

    # build list from search matches on first system
    for i in range(0, len(file_list1)):
        if prefix in file_list1[i]:
            # break?
            return_list1.append(file_list1[i])
            file1_loc = str(file_list1[i])

    # ensures first file is closed
    f.close()

    # locate correct second file based on key
    if key2 in system1:
        with open(pallasDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file2 = f.readlines()

    if key2 in system2:
        with open(minervaDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file2 = f.readlines()

    if key2 in system3:
        with open(athenaDir, 'r', encoding='utf - 8',
                  errors='ignore') as f:
            file2 = f.readlines()

    # build list from second system file
    for i in file2:
        file_list2.append(i)

    # build list from search matches on second system
    for i in range(0, len(file_list2)):
        if prefix in file_list2[i]:
            # break?
            return_list2.append(file_list2[i])
            file2_loc = str(file_list2[i])

    # ensures second file is closed
    f.close()

    matchList = []
    matchList2 = []

    for i in range(len(return_list2)):
        if return_list2[i] not in return_list1:
            matchList.append(return_list2[i])

    for i in range(len(return_list1)):
        if return_list1[i] not in return_list2:
            matchList2.append(return_list1[i])

    # print key matches that are not found on either system (probably not needed, but kept for thoroughness)
    if len(return_list1) < 1 & len(return_list2) < 1:
        for i in return_list1:
            print(return_list1[i] + 'is not on system 1')
        for i in return_list1:
            print(return_list1[i] + 'is not on system 2')

    # if matches are found on both systems, notify the user and print results from both systems
    # client can edit out block (lines 122-129) if only files/matches unique to each system are preferred
    elif len(return_list1) >= 1 & len(return_list2) >= 1:
        print('Search for ' + prefix + ' produced matches on both systems. Results are below:\nSYSTEM '
                                       '1 MATCHES:\n ')
        for i in range(0, len(return_list1)):
            print(str(return_list1[i]))
        print("SYSTEM 2 MATCHES:\n")
        for i in range(0, len(return_list2)):
            print(str(return_list2[i]))

        # print matches unique to each system
        if len(matchList) >= 1:
            print('\n' + 'Matches found on System 1 that differ from matches found on System 2' + '\n')
            for i in range(0, len(matchList)):
                print(str(matchList[i]))
        if len(matchList2) >= 1:
            print('\n' + 'Matches found on System 2 that differ from matches found on System 1' + '\n')
            for i in range(0, len(matchList2)):
                print(str(matchList2[i]))

    # if matches are not found on system 1, print those files and notify the user
    elif len(return_list1) >= 1 & len(return_list2) < 1:
        for i in range(0, len(return_list2)):
            print(str(return_list2[i]) + 'is not on system 1')
    # if matches are not found on system 2, print those files and notify the user
    elif len(return_list1) < 1 & len(return_list2) >= 1:
        for i in range(0, len(return_list1)):
            print(str(return_list1[i]) + 'is not on system 2')
    # if no matches are found, provide a message that notifies the user
    else:
        print("No matches found on either system")


findfile()
