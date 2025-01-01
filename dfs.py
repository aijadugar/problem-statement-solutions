# Depth-First Search using recursion
def dfs_recursive(graph, node, visited):
    if visited is None:
        return ''
    
    visited.append(node)
    print(node, end=' ')
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            dfs_recursive(graph, neighbor, visited)
            

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS traversal:")
dfs_recursive(graph, 'A', visited=[])
