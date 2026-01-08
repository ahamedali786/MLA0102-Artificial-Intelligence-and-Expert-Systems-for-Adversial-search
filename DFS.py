def dfs(graph, start, visited=None): 2 usages
if visited is None:
visited = set()
visited. add (start)
print (start, end=" ") for neighbor in graph [start]: if neighbor not in visited:
dfs (graph, neighbor, visited)
graph =仔
n = int(input"Enter number of nodes: "))
for i in range(n):
node = input("Enter node: ")
I
neighbors = input(f"Enter neighbors of {node} (space-separated): "). split()
graph [nodel = neighbors
start = input("Enter starting node:
")
print("DFS Traversal:")
dfs (graph, start)

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
DFS Traversal: 1 2 3 4 5 6 7 8 9 10

       
