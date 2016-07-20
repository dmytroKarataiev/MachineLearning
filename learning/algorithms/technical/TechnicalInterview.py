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
        return None

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


def checkQuestion2():
    strings = ["olenaanelo", "dimaamdi", "udacity", "udaudacityytic", "aaabbbbccc"]
    for word in strings:
        print question2(word)
    print "-------------"


# Question 2
# add biggest
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.
def question2(a):
    """
    Given a string a, find the longest palindromic substring contained in a.
    :param a: initial string
    :return: longest palindromic substring in a
    """

    biggest = (0, "")

    for num in range(len(a)):
        for iter in range(num + 1, len(a)):
            check = a[num:iter]
            if len(check) > biggest[0] and isPalindrome(check):
                biggest = (len(check), check)

    return biggest


def isPalindrome(s):
    """
    Checks if a string is a palindrome
    :param s: initial string
    :return: True if palindrome, False - otherwise
    """
    if len(s) < 1:
        return True

    for num in range(len(s)):
        if s[num] != s[len(s) - num - 1]:
            return False

    return True


# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m), where ll is the first node of a linked list
# and m is the "mth number from the end". You should copy/paste the Node class below
# to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def findFromEnd(self, position):
        nodesList = []

        current = self.head

        while current:
            nodesList.append(current)
            current = current.next

        if position >= len(nodesList):
            # todo raise ValueError("Should be smaller than the len of the LL")
            return None

        return nodesList[-(position + 1)]


def checkQuestion3():
    # Test cases
    # Set up some Elements
    ll = LinkedList()

    for node in range(1, 11):
        ll.append(Node(node))

    cases = [0, 1, 2, 3, 9, 11, 10, 12]
    for case in cases:
        out = ll.findFromEnd(case)
        if out is not None:
            print "Case:", case, out.data



def main():
    try:
        checkQuestion1()
        checkQuestion2()
        checkQuestion3()
    except ValueError, e:
        print e


if __name__ == '__main__':
    main()
