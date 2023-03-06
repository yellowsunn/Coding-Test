import sys


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


def union_all(persons):
    for i in range(len(persons) - 1):
        union(persons[i], persons[i + 1])


def has_known(persons):
    parent_set = set(find_parent(known) for known in knowns)
    for person in persons:
        p = find_parent(person)
        if p in parent_set:
            return True
    return False


input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
knowns = list(map(int, input().split()))[1:]
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

union_all(knowns)
for party in parties:
    union_all(party)

result = 0
for party in parties:
    if not has_known(party):
        result += 1
print(result)
