def reverse_sentences(sentence):
    words = sentence.split(' ')
    words.reverse()

    return ' '.join(words)


def test_reverse():

    sent = "The revolution will not be televised"
    assert(reverse_sentences(sent) == "televised be not will revolution The")

    print("Test passed!!")


if __name__ == "__main__":
    test_reverse()
