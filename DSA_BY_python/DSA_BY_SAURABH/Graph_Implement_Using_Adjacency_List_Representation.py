import Queue_Using_List_ as now
class Graph:
    def __init__(self,vno) -> None:
        self.vertex_count = vno
        self.dict_list = {i:list() for i in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.dict_list[u].append((v,weight))
            self.dict_list[v].append((u,weight))
        else:
            print("Invalid Vertex")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.dict_list[u] = [(vertex,weight) for vertex,weight in self.dict_list.values() if vertex != v]
            self.dict_list[v] = [(vertex,weight) for vertex,weight in self.dict_list.values() if vertex != u]
        else:
            print("Invalid Vertex")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex == v for vertex,x in self.dict_list[u])
        else:
            print("Invalid Vertex")
    
    def print_dict_list(self):
        for vertex,n in self.dict_list.items():
            print(f"V{vertex} : {n}")
    
    
    def BFS_Traversal(self,start):
        queue = now.Queue()
        visit = [0]*self.vertex_count
        queue.enqueue(start)
        visit[start] = 1
        while not queue.is_empty():
            n = queue.get_front()
            print(n,end=" ")
            queue.dequeue()
            for i,(vertex,weight) in enumerate(self.dict_list[n]):
                if visit[vertex] == 0:
                    queue.enqueue(vertex)
                    visit[vertex] = 1
    
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    
    g.print_dict_list()
    print("BFS Traversal")
    g.BFS_Traversal(0)