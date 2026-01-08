from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter neighbors: ").split()
    graph[vertex] = neighbors

start_node = input("Enter starting node: ")

if start_node not in graph:
    print("Error: Starting node not present in graph")
else:
    bfs(graph, start_node)

OUTPUT:
Enter number of vertices: 10
Enter vertex: 1
Enter neighbors: 2 7
Enter vertex: 2
Enter neighbors: 3 6
Enter vertex: 3
Enter neighbors: 4 5
Enter vertex: 4
Enter neighbors: 
Enter vertex: 5
Enter neighbors: 
Enter vertex: 6
Enter neighbors: 
Enter vertex: 7
Enter neighbors: 8 10
Enter vertex: 8
Enter neighbors: 9
Enter vertex: 9
Enter neighbors: 
Enter vertex: 10
Enter neighbors: 
Enter starting node: 1
BFS Traversal: 1 2 7 3 6 8 10 4 5 9 
