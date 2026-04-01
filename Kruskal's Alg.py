class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Cycle detected

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# Example usage
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

mst, total = kruskal(vertices, edges)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total weight:", total)