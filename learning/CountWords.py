import operator

"""Count words."""


def count_words(s, n):
    """Return the n most frequently occurring words in s."""

    # Count the number of occurrences of each word in s
    dictionary = {}
    s = s.split(" ")
    for word in s:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    # Sort the occurences in descending order (alphabetically in case of ties)
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(0))
    sorted_x = sorted(sorted_x, key=operator.itemgetter(1), reverse=True)

    # Return the top n words as a list of tuples (<word>, <count>)
    output = []
    for number in range(n):
        output.append(sorted_x[number])

    return output


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat cat cat bat bat bat a a b b b cats cats cats", 3)
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
