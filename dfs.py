graph = {
 'A' : ['B','C'],
 'B' : ['D','E'],
 'C' : ['F','G'],
 'D' : ['H','I'],
 'E' : ['J','K'],
 'F' : ['L','M'],
 'G' : ['N','O'],
 'H' : [],
 'I' : [],
 'J' : [],
 'K' : [],
 'L' : [],
 'M' : [],
 'N' : [],
 'O' : [], 
}
visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node): #function for dfs 
 if node not in visited:
  print (node)
  visited.add(node)
 for neighbour in graph[node]:
   dfs(visited, graph, neighbour)
# Main Program
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')