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
    if s == None or t == None or \
                    len(t) == 0 or len(s) == 0 or len(t) > len(s):
        # "Strings should be of len > 0 or t < s"
        return None

    if t in s:
        return True
    else:
        return False


def checkQuestion1():
    s = ["udacity", 'udddda']
    t = ["udatyci", "ud", "du", "ad", "da", "city", "ncity", "uda", "", None]
    # answers for s[0]: F, T, F, F, T, T, F, T, None
    # answers for s[1]: None, T, F, F, T, F, F, F, None

    for word in s:
        print "Is substring of " + word + ": word \\ boolean"
        for each in t:
            print str(each) + " \\ " + str(question1(word, each))


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

    if a == None:
        return None
    elif len(a) < 2:
        return a

    biggest = (0, "")

    for num in range(len(a)):
        for iter in range(num + 1, len(a)):
            check = a[num:iter]
            if len(check) > biggest[0] and check == check[::-1]:
                biggest = (len(check), check)

    return biggest[1]


def checkQuestion2():
    strings = ["olenaanelo", "dimaamdi", "udacity", "udaudacityytic", "aaabbbbccc", "a", "", None]
    # answers: lenaanel, maam, u, ityyti, bbbb

    print "Biggest palindromic substring: word \\ substring"
    for word in strings:
        print word, "\\", question2(word)


# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
#
# Vertices are represented as unique strings. The function definition should be question3(G)

# code
parent = dict()
rank = dict()


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


def question3(graph):
    for vertices in graph.keys():
        make_set(vertices)

    min_spanning_tree = {}

    edges = []
    for key in graph:
        for element in graph[key]:
            edges.append((element[1], key, element[0]))

    edges.sort()
    for edge in edges:
        wt, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)

            if v1 in min_spanning_tree:
                min_spanning_tree[v1].append((v2, wt))
            else:
                min_spanning_tree[v1] = [(v2, wt)]

            if v2 in min_spanning_tree:
                min_spanning_tree[v2].append((v1, wt))
            else:
                min_spanning_tree[v2] = [(v1, wt)]
    return min_spanning_tree


def checkQuestion3():
    G = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
         'C': [('A', 10), ('B', 5)],
         'D': [('A', 5), ('B', 3)]}

    # Empty tree
    G2 = {}

    # Only 2 nodes
    G3 = {'A': [('B', 2)]}

    # (A) - 5 - (B)
    #  |  \   /  |
    #  5    1    5
    #  | /     \ |
    # (D) - 5 - (C)
    # Answer: A - C - B - D
    G4 = {'A': [('B', 5), ('C', 1), ('D', 5)],
          'B': [('A', 5), ('C', 5), ('D', 1)],
          'C': [('A', 1), ('B', 5), ('D', 5)],
          'D': [('A', 5), ('B', 1), ('C', 5)]}

    trees = [G, G2, G3, G4]

    for tree in trees:
        print "Minimum Spanning Tree:", question3(tree)


# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
# For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents
# of the root's left child, then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
# r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing
# the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
#
# and the answer would be 3.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = root

    def searchCommon(self, n1, n2):
        root1 = self.getPath(n1)
        root2 = self.getPath(n2)

        for element in root1[::-1]:
            if element in root2:
                return element.value

        return -1

    def getPath(self, node):
        current = self.root

        ancestors = [current]

        while current:
            if node < current.value:
                if current.left:
                    current = current.left
                    ancestors.append(current)
            elif node > current.value:
                if current.right:
                    current = current.right
                    ancestors.append(current)
            else:
                return ancestors

    def search(self, find_val):
        current = self.root

        while current:
            if find_val < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            elif find_val > current.value:
                if current.right:
                    current = current.right
                else:
                    return False
            else:
                return True
        return False


def question4(tree, root, node1, node2):
    if node1 > len(tree) or node2 > len(tree) or root > len(tree):
        return None
        # "Incorrect input, nodes should be present in the tree"

    nodes = [None] * len(tree)

    # O(len(tree))
    for each in range(len(tree)):
        nodes[each] = Node(each)

    # O(len(tree)^2)
    for each in range(len(tree)):
        for element in range(len(tree)):
            if tree[each][element] == 1:
                if nodes[each].value > element:
                    nodes[each].left = nodes[element]
                else:
                    nodes[each].right = nodes[element]

    bst = BST(nodes[root])

    # if node are present in the BST, then try to find a common ancestor
    # search is in O(log(n))
    # searchCommon is in O(log(n))
    if bst.search(node1) and bst.search(node2):
        return bst.searchCommon(node1, node2)
    else:
        return None
        # "Not found"


def checkQuestion4():
    tree = [[0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]]

    question4(tree, 3, 1, 4)
    question4(tree, 3, 1, 0)

    #          (3)
    #       /       \
    #     (1)       (6)
    #   /    \      /  \
    # (0)   (2)   (5)  (7)
    #             /
    #           (4)
    #
    tree = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print "Least common ancestor: "
    tests = [(3, 5, 7), (3, 4, 7), (3, 4, 5), (3, 1, 7), (3, 2, 0), (9, 2, 0), (3, 12, 5)]

    for each in tests:
        print "root:", each[0], "node1:", each[1], "node2", each[2], "lca:", question4(tree, each[0], each[1], each[2])
        # Answers: 6, 6, 5, 3, 1


# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m), where ll is the first node of a linked list
# and m is the "mth number from the end". You should copy/paste the Node class below
# to use as a representation of a node in the linked list. Return the value of the node at that position.

class Element(object):
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
        nodesNum = 0

        current = self.head

        while current:
            nodesNum += 1
            current = current.next

        current = self.head

        if position >= nodesNum:
            return None
            # "Should be smaller than the len of the LL"

        position = nodesNum - position

        while position > 1:
            current = current.next
            position -= 1

        return current


def checkQuestion5():
    # Test cases
    # Set up some Elements
    ll = LinkedList()

    for node in range(1, 11):
        ll.append(Element(node))

    cases = [0, 1, 2, 3, 9, 11, 10, 12]
    answers = [10, 9, 8, 7, 1, None, None, None]
    print "Node from the end of a LinkedList: n from end \\ value"
    for case in range(len(cases)):
        out = ll.findFromEnd(cases[case])
        if out is None:
            print "Case:", case, out, "Should be:", answers[case]
        else:
            print "Case:", case, "\\", out.data, "Should be:", answers[case]


def main():
    checks = [checkQuestion1, checkQuestion2, checkQuestion3, checkQuestion4, checkQuestion5]

    for each in range(len(checks)):
        print "Checking question #" + str(each + 1) + "\n"
        checks[each]()
        print "---------------"


if __name__ == '__main__':
    main()
