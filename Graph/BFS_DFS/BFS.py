# from collections import deque


# def bfs(V, adj):
#     bfs = []
#     visiter = [False] * V
#     queue = deque()
#     queue.append(0)
#     visiter[0] = True
#     while queue:
#         node = queue.popleft()
#         bfs.append(node)
#         for i in adj[node]:
#             if not visiter[i]:
#                 queue.append(i)
#                 visiter[i] = True
#     return bfs


# # Sample usage
# if __name__ == "__main__":
#     V = 5
#     adj = [[] for _ in range(V)]
#     adj[0].append(1)
#     adj[0].append(2)
#     adj[0].append(3)
#     adj[2].append(4)
#     ans = bfs(V, adj)
#     print(ans)


from collections import deque

class GraphBFS:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self, start_node):
        bfs_result = []
        visited = [False] * self.V
        queue = deque()
        queue.append(start_node)
        visited[start_node] = True

        while queue:
            node = queue.popleft()
            bfs_result.append(node)
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return bfs_result

# Sample usage
if __name__ == "__main__":
    V = 5
    graph = GraphBFS(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(2, 4)

    start_node = 0
    bfs_result = graph.bfs(start_node)
    print("BFS result:", bfs_result)

