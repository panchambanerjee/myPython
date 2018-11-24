import string


def anagram_check(str1, str2):
    anagram_table = {key: 0 for key in string.ascii_lowercase}

    for i in str1:
        anagram_table[i] += 1

    for i in str2:
        anagram_table[i] -= 1

    if len(set(anagram_table.values())) < 2:
        return True
    else:
        return False


def test_anagram():
    str1 = 'ocean'
    str2 = 'naeco'
    assert(anagram_check(str1, str2) is True)

    str1 = 'bob'
    str2 = 'sideshow'
    assert(anagram_check(str1, str2) is False)

    print('Tests passed!!')


if __name__ == "__main__":
    test_anagram()
