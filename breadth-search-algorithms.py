graph = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F','G'],
 'D' : [],
 'E' : [],
 'F' : [],
 'G' : [],
}
visited = [] # List for visited nodes.
queue = [] #Initialize a queue
def bfs(visited, graph, node): 
#It adds the node to the visited list
# used to keep track of which nodes have already been explored.
 visited.append(node)
#determines which node to explore next, in BFS order.
 queue.append(node)
# Creating loop to visit each node
 while queue: 
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, 'A') 