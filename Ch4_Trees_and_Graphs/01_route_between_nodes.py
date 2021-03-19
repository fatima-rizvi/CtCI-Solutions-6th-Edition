def routeBetweenNodes(graph, s, e):
    n = len(graph)
        
    ans = []
        
    visited = set()   
    temp = [0]

    for child in graph[0]:
        dfs(child, temp[:], ans, graph, n)
        
    found = False
    for route in ans:
      if route[0] == s.value:
        if route[-1] == e.value:
          found = True
          
    if found:
      return True
    return False
            
    
def dfs(start, temp, ans, graph, n):
    if start == n-1:
        temp.append(start)
        ans.append(temp[:])
        return

    temp.append(start)

    for child in graph[start]:
        dfs(child, temp[:], ans, graph, n)
