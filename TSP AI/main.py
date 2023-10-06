from sys import maxsize
from itertools import permutations

V = int(input("Enter the number of nodes: "))

def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    min_path_indices = []

    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        path_indices = []
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            path_indices.append((k, j))
            k = j
        current_pathweight += graph[k][s]
        path_indices.append((k, s))

        if current_pathweight < min_path:
            min_path = current_pathweight
            min_path_indices = path_indices

    return min_path, min_path_indices
#Driver code
g = []
for a in range(V):
    col = []
    for b in range(V):
        if a != b:
            ele = int(input("Enter the weight of the edge " + str(a) + " to " + str(b) + ": "))
            col.append(ele)
        else:
            col.append(0)
    g.append(col)

s = int(input("Enter the starting node: "))
min_weight, min_path_indices = travellingSalesmanProblem(g, s)

print("Path:")
for u, v in min_path_indices:
    print(f"Node {u} to Node {v}, Weight: {g[u][v]}")
print("Minimum Weight:", min_weight)


# Function to calculate factorial
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# # Function to generate permutations
# def generate_permutations(arr):
#     n = len(arr)
#     total_permutations = factorial(n)
#
#     permutations = []
#     for i in range(total_permutations):
#         p = []
#         temp = i
#         for j in range(n):
#             div = factorial(n - 1 - j)
#             index = temp // div
#             temp = temp % div
#             p.append(arr.pop(index))
#         permutations.append(p)
#     return permutations
#
#
# V = int(input("Enter the number of nodes: "))
#
#
# def travellingSalesmanProblem(graph, s):
#     vertex = []
#     for i in range(V):
#         if i != s:
#             vertex.append(i)
#
#     min_path = float("inf")
#     min_path_indices = []
#
#     next_permutation = generate_permutations(vertex)
#     for i in next_permutation:
#         current_pathweight = 0
#         path_indices = []
#         k = s
#         for j in i:
#             current_pathweight += graph[k][j]
#             path_indices.append((k, j))
#             k = j
#         current_pathweight += graph[k][s]
#         path_indices.append((sk, s))
#
#         if current_pathweight < min_path:
#             min_path = current_pathweight
#             min_path_indices = path_indices
#
#     return min_path, min_path_indices


g = []
for a in range(V):
    col = []
    for b in range(V):
        if a != b:
            ele = int(input("Enter the weight of the edge " + str(a) + " to " + str(b) + ": "))
            col.append(ele)
        else:
            col.append(0)
    g.append(col)

s = int(input("Enter the starting node: "))
min_weight, min_path_indices = travellingSalesmanProblem(g, s)

print("Minimum Weight:", min_weight)
print("Path:")
for u, v in min_path_indices:
    print(f"Node {u} to Node {v}, Weight: {g[u][v]}")
