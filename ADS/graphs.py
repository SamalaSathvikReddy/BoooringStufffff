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
