# This is the Undirected Graph
import Queue_Using_List_ as now
class Graph:
    def __init__(self,vno) -> None:
        self.vertex_count = vno
        self.adj_matrix = [ [0]*vno for e in range(vno)]
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex")
    
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))
    

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(3,4)
    
    g.print_adj_matrix()
    