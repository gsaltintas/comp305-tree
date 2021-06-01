
class Vertex:
    def __init__(self, weight: int, id: int = None):
        """ 
        :param weight: weight of the vertex
        :param id: i, ie. the order vertex appears when adding to the tree
        """
        self.weight = weight
        self.id = id
        self.neighbors = []

    def add_neighbor(self, v):
        self.neighbors.append(v)

    def remove_yourself(self):
        for neighbor in self.neighbors:
            neighbor.neighbors.remove(self)
        self.neighbors = []        

    def __str__(self) -> str:
        return (f"Vertex {self.id}: {self.weight}")


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex):
        self.v1 = v1
        self.v2 = v2
        v1.add_neighbor(v2)
        v2.add_neighbor(v1)


class Tree:
    def __init__(self, node_no: int = 0):
        self.node_no = node_no
        self.vertices = []

    def add_vertex(self, v: Vertex):
        self.vertices.append(v)

    def add_edge(self, v1: int, v2: int) -> Edge:
        """ adds an edge between vertices with indices v1 and v2 """
        return Edge(self.vertices[v1], self.vertices[v2])

    def dfs_order(self) -> (list,list):
        """ iterates over the tree's vertices with DFS and returns the list of dfs order """
        visited = []
        count = [0]*(len(self.vertices))
        return self.dfs_util(self.root, visited,count)

    def dfs_util(self, v, visited,count) -> (list,list):
        count[self.vertices.index(v)]=1
        visited.append(v)
        for neigh in v.neighbors:
            if neigh not in visited:
                self.dfs_util(neigh, visited,count)
                count[self.vertices.index(v)]+=count[self.vertices.index(neigh)]
            
        return (visited,count)

    @property
    def root(self) -> Vertex:
        return self.vertices[0]

    def __str__(self) -> str:
        s = ""
        for i in range(self.node_no):
            s += str(self.vertices[i]) + "\n"
        return s
