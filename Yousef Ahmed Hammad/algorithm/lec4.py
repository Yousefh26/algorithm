def is_bipartite(graph):
    color = {} 
    for node in graph:
        if node not in color:
            queue = [node]
            color[node] = 0
            while len(queue) > 0:
                curr = queue.pop(0)
                for team in graph[curr]:
                    if team not in color:
                        color[team] = 1 - color[curr]
                        queue.append(team)
                    elif color[team] == color[curr]:
                        return False
    return True