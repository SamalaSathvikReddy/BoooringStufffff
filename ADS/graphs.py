class Graph:
    def __init__(self, num_vertices):
        self.graph = dict()

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = [u] 
        else:
            self.graph[v].append(u)

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
    
    def adjacent_nodes(self, node):
        return self.graph[node] 

    def unconnected_vertices(self):
        st = set() 
        for k in self.graph:
            for v in self.graph[k]:
                if v not in self.graph:
                    st.insert(v)

        li = []
        for v in st:
            li.append(v)
        return li

    def bfs(self, val):
        Que = []
        Vis = []
        Que.append(val)

        while len(Que) > 0:
            front = Que[0]
            Que = Que[1:]
            Vis.append(front)
             
            if front in self.graph: 
                for v in self.graph[front]:
                    if v not in Que and v not in Vis:
                        Que.append(v)

        return Vis

    def dfs(self, st_vertex):
        li = []

        dfs_r(li , st_vertex)

        return li

    def dfs_r(self, visited , cur_vertex):
        visited.append(cur_vertex)
        if cur_vertex in self.graph:

            for v in self.graph[cur_vertex]:
                if v not in li:
                    dfs_r(visited, v)


