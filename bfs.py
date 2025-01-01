# # Breadth-First Search using recursion in a single function
# def bfs_recursive(graph, queue, visited):
#     if not queue:
#         return
    
#     node = queue.pop(0)
#     print(node, end=' ')
    
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)
    
#     bfs_recursive(graph, queue, visited)

# # Example usage:BFS traversal: A B C D E F 

# print("BFS traversal:")
# start_node = 'A'
# bfs_recursive(graph, queue= [start_node],visited= set([start_node]))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, v, q):
    if not q: 
        return ''
    
    node = q.pop(0)
    print(node, end= " ->")
    
    for neighbour in graph[node]:
        if neighbour not in v:
            v.append(neighbour)
            q.append(neighbour)
            bfs(graph, v, q)

root = 'A'
bfs(graph, v = [root], q = [root])