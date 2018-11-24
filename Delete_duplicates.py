# Script to find and delete duplicate characters in a string

import string


def delete_duplicates(str1):
    char_table = {key: 0 for key in string.ascii_lowercase}

    for i in str1:
        char_table[i] += 1

    for k, v in char_table.items():
        if v > 1:
            str1 = str1.replace(k, " ")

    return str1


if __name__ == "__main__":
    print(delete_duplicates("yahoo"))