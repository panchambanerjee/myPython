from collections import Counter


def find_recurring_words(seq, n):
    counter = Counter()
    for word in seq.split():
        counter[word] += 1
    return counter.most_common(n)


if __name__ == "__main__":
    print(find_recurring_words("ringo ringo paul dead piggies george paul paul ringo john", 3))
    print()
    print(find_recurring_words("ringo ringo paul dead piggies george paul paul ringo john", 2))