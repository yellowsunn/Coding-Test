# https://www.acmicpc.net/problem/14425

import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, is_end):
        self.is_end = is_end
        self.children = {}


class Trie(object):
    def __init__(self):
        self.parent = Node(False)

    def insert(self, word):
        cur_node = self.parent
        for w in word:
            if w not in cur_node.children:
                cur_node.children[w] = Node(False)
            cur_node = cur_node.children[w]
        cur_node.is_end = True

    def search(self, word):
        cur_node = self.parent
        for w in word:
            if w in cur_node.children:
                cur_node = cur_node.children[w]
            else:
                return False
        return cur_node.is_end


n, m = map(int, input().split())
my_trie = Trie()

for _ in range(n):
    my_trie.insert(input().rstrip())

count = 0
for _ in range(m):
    if my_trie.search(input().rstrip()):
        count += 1
print(count)
