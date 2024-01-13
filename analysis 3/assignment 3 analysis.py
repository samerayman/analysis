from collections import deque, defaultdict

def parse_graph(adj_list):
    """Parse the adjacency list into a graph dictionary."""
    graph = defaultdict(list)
    for line in adj_list:
        node, *edges = map(int, line.split())
        graph[node] = edges
    return graph

def dfs(graph, start):
    """Perform Depth-First Search and return traversal order and cycle information."""
    visited, stack = set(), [start]
    traversal, cycle_detected = [], False
    parent = {start: None}

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(set(graph[vertex]) - visited)

            # Check for back edge indicating a cycle
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                elif parent[vertex] != neighbor:
                    cycle_detected = True

    return traversal, cycle_detected

def bfs(graph, start):
    """Perform Breadth-First Search and return traversal order and bipartiteness information."""
    visited, queue = set(), deque([start])
    traversal, bipartite, colors = [], True, {start: 0}

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            current_color = colors[vertex]

            for neighbor in graph[vertex]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    bipartite = False

    return traversal, bipartite

# Define the adjacency list
adj_list = ["1 3 4", "2 1 3", "3 4", "4 1 2"]

# Parse the graph
graph = parse_graph(adj_list)

# Perform DFS and BFS
dfs_traversal, cycle_detected = dfs(graph, 1)
bfs_traversal, is_bipartite = bfs(graph, 1)

print("DFS Traversal:", dfs_traversal)
print("Cycle Detected in DFS:", cycle_detected)
print("BFS Traversal:", bfs_traversal)
print("Graph is Bipartite:", is_bipartite)
