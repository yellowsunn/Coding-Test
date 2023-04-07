# https://www.acmicpc.net/problem/1991

import sys

input = sys.stdin.readline


def pre_order(node):
    if node == '.':
        return ''
    word = node
    word += pre_order(tree[node][0])
    word += pre_order(tree[node][1])
    return word


def in_order(node):
    if node == '.':
        return ''
    word = in_order(tree[node][0])
    word += node
    word += in_order(tree[node][1])
    return word


def post_order(node):
    if node == '.':
        return ''
    word = post_order(tree[node][0])
    word += post_order(tree[node][1])
    word += node
    return word


n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]

print(pre_order('A'))
print(in_order('A'))
print(post_order('A'))
