# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.
def question1(s, t):
    """
    Given two strings s and t, determine whether some anagram of t is a substring of s.
    For example: if s = "udacity" and t = "ad", then the function returns True.
    :param s: initial string
    :param t: substring of s
    :return: True if t is substring of, False otherwise.
    """

    if len(s) == 0 or len(t) == 0:
        # todo raise ValueError("Strings should be of len > 0")
        return False

    frequency = {}
    for letter in s:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    for letter in t:
        if letter in frequency and frequency[letter] > 0:
            frequency[letter] -= 1
        else:
            return False

    return True


def checkQuestion1():
    s = "udacity"
    t = ["udatyci", "ud", "du", "ad", "da", "city", "ncity", ""]

    print "Checking Q1:"
    for word in t:
        print word, question1(s, word)
    print "-------------"

def checkQ2():
    strings = ["olenaanelo", "dimaamdi", "udacity", "udaudacityytic", "aaabbbbccc"]
    for word in strings:
        question2(word)
    #question2("abcdef")
    print "---"
    #question2("abccba")


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.
def question2(a):
    """
    Given a string a, find the longest palindromic substring contained in a.
    :param a: initial string
    :return: longest palindromic substring in a
    """
    start = end = length = -1

    stringLen = len(a)

    for number in range(stringLen):
        #print a[number], a[stringLen - number - 1]
        if (a[number] == a[stringLen - number - 1]):
            if (end == -1):
                length = 1
                end = stringLen - number
                start = stringLen - number - 1
            else:
                start -= 1
                length += 1

        else:
            start = stringLen - number
            end = -1

    print end, length, start
    if end != -1:
        substring = a[start:end]
        out = ""
        for letter in range(len(substring)):
            out += substring[len(substring) - letter - 1]

        print out


def main():
    #checkQuestion1()
    checkQ2()


if __name__ == '__main__':
    main()