'''
Neighbours[]:
1: 2, 5
2: 1, 6
3: 7
4: 5, 8
5: 1, 4, 8
6: 2, 7, 9
7: 3, 6, 10
8: 4, 5, 9
9: 6, 8
10: 6, 7 
'''

class Node:
    def __init__(self, n):
        self.name = n
        self.neighbours = list()
        self.distance = -1
        self.visited = False
    
    def addNeighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Graph:
    nodes = {}

    def addNode(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        
        return False

    def addEdge(self, u, v):
        if u in self.nodes and v in self.nodes:
            for key, value in self.nodes.items():
                if key == u:
                    value.addNeighbour(v)
                if key == v:
                    value.addNeighbour(u)
            return True
        
        return False

    def printGraph(self):
        values = []
        for key in sorted(list(self.nodes.keys())):
            print(f"{key} {self.nodes[key].neighbours} {self.nodes[key].distance}")
            values.append(self.nodes[key].distance)
        return values

    def bfs(self, node: Node):
        q = list()
        node.distance = 0
        node.visited = True

        for n in node.neighbours:
            self.nodes[n].distance = node.distance + 6
            q.append(n)

        while len(q) > 0:
            u = q.pop(0)
            node_u: Node = self.nodes[u]
            node_u.visited = True

            for v in node_u.neighbours:
                node_v: Node = self.nodes[v]
                if node_v.visited == False:
                    q.append(v)
                    if node_v.distance > node_u.distance + 6 or node_v.distance == -1:
                        node_v.distance = node_u.distance + 6

if __name__ == '__main__':
    g= Graph()
    edges = [
        [1,2],
        [1,5],
        [2,1],
        [2,6],
        [3,7],
        [4,5],
        [4,8],
        [5,1],
        [5,4],
        [5,8],
        [6,2],
        [6,7],
        [6,9],
        [6,10],
        [7,3],
        [7,6],
        [7,10],
        [8,4],
        [8,5],
        [8,9],
        [9,6],
        [9,8],
        [10,6],
        [10,7]
        ]

    for i in range (1, max(max(edges)) + 1):
        g.addNode(Node(i))

    for edge in edges:
        g.addEdge(edge[0], edge[1])


    g.bfs(g.nodes[10])
    out = g.printGraph()
    print(out)

    # print(max(max(edges)))