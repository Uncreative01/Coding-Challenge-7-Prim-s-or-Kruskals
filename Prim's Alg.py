import heapq

def prim(graph, start):

    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent)
    
    mst = []
    total_weight = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst.append((parent, current, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst, total_weight


# Example usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2), ('D', 4)],
    'C': [('A', 3), ('B', 2), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total weight:", total)