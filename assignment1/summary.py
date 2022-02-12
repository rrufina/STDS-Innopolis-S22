from node import Node

class Summary:
    def __init__(self, eps):
        self.n = 0
        self.s = 0
        self.tuples = []
        self.eps = eps
        
    def find_r(self, node):
        idx = self.tuples.index(node)
        r_min = 0
        for i in range(0, idx+1):
            r_min += self.tuples[i].g
        r_max = r_min+self.tuples[idx].delta
        return r_min, r_max

    def quantile(self, q):
        n = self.n
        r = q*n
        for node in self.tuples:
            r_min, r_max = self.find_r(node)
            if r-r_min <= self.eps*n and r_max-r <= self.eps*n:
                return node.v

        # if such value was not found
        result_nodes = []
        for node in self.tuples:
            r_min, r_max = self.find_r(node)
            if r-r_min <= self.eps*n:
                result_nodes.append([node, r_max])
        result_nodes = sorted(result_nodes, key=lambda x: x[1])
        return result_nodes[0][0].v 

    def insert(self, v):
        if len(self.tuples)==0:
            node = Node(v, 1, 0)
            self.tuples.append(node)
        elif v < self.tuples[0].v:
            node = Node(v, 1, 0)
            self.tuples.insert(0, node)
        elif v >= self.tuples[-1].v:
            node = Node(v, 1, 0)
            self.tuples.append(node)
        else:
            for i in range(self.s-1, -1, -1):
                if self.tuples[i].v <= v:
                    node = Node(v, 1, 2*self.eps*self.n)
                    self.tuples.insert(i+1, node)
                    break
        self.s+=1
        self.n+=1

    def delete(self, node):
        idx = self.tuples.index(node)
        next_node = self.tuples[idx+1]
        new_node = Node(next_node.v, node.g+next_node.g, next_node.delta)
        self.tuples[idx+1] = new_node
        del self.tuples[idx]
        self.s-=1

    def compress(self):
        i = self.s-2
        while i > -1:
            #print(i)
            if i>=self.s-1:
                i=self.s-2
            
            node = self.tuples[i]
            descendants, g_sum, idx_node = node.get_descendants(self.tuples, self.n, self.eps)
            next_node = self.tuples[i+1]
            if node.delta != 0:
                if node.band(self.n, self.eps) <= next_node.band(self.n, self.eps) and g_sum+next_node.g+next_node.delta < 2*self.eps*self.n:
                    #print("Yeeah I delete it")
                    i = idx_node
                    for des in descendants:
                        self.delete(des)
                else:
                    i-=1
            else:
                i-=1