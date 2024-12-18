def dijkstra(graph,start,goal):
    unvisited={n:float('inf') for n in graph.keys()}
    unvisited[start]=0
    visited={}
    
    while unvisited:
        minNode=min(unvisited, key=unvisited.get)
        visited[minNode]=unvisited[minNode]
        
        if minNode==goal:
            break
        
        for neighbor in graph.get(minNode):
            if neighbor in visited:
                continue
            tempDist=unvisited[minNode]+graph[minNode][neighbor]
            if tempDist < unvisited[neighbor]:
                unvisited[neighbor]=tempDist
        
        unvisited.pop(minNode)
    print(f'{visited=}')


myGraph={
    'A':{'C':3,'D':4,'E':4},
    'B':{'C':2,'F':2},  
    'C':{'A':3,'B':2,'E':4,'F':5,'G':5},
    'D':{'A':4,'E':2},
    'E':{'A':4,'C':4,'D':2,'G':5},
    'F':{'B':2,'C':5,'G':5},
    'G':{'C':5,'E':5,'F':5}
}

dijkstra(myGraph,'','C')
