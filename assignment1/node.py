import math

class Node:
    
    def __init__(self, v, g, delta):
        self.v = v
        self.g = g
        self.delta = delta

    def get_descendants(self, tuples, n, eps):
        descendants = []
        band_value = self.band(n, eps)
        g_sum = 0


        # find nodes with v less than current
        sorted_v = sorted(tuples, key=lambda node: node.v, reverse=True)
        self_index = sorted_v.index(self)
        for i in range(self_index, -1, -1):
            if sorted_v[i].v==self.v:
                continue
            else:
                break
        descendants = sorted_v[i+1:]
        if not descendants:
            return [], 0, -1


        # find nodes with delta greater than current
        sorted_deltas = sorted(descendants, key=lambda node: node.delta)
        self_index = sorted_deltas.index(self)
        for i in range(self_index, -1, -1):
            if sorted_deltas[i].delta==self.delta:
                continue
            else:
                break
        #if i < n:
        descendants = sorted_deltas[i+1:]
        if not descendants:
            return [], 0, -1



        # find nodes with band less than current and calculate g sum
        for node in descendants:
            if node.band(n, eps)<band_value:
                g_sum+=node.g
            else:
                descendants.remove(node)

        # find tuple that will be iterated next in compress 
        idxs = list(map(lambda node: tuples.index(node), descendants))
        self_index = tuples.index(self)
        if self_index not in idxs:
            self_index-=1
        else:
            while self_index in idxs:
                self_index-=1
        
        return sorted(descendants, key=lambda node: node.v, reverse=True), g_sum, self_index

    def band(self, n, eps):
        max_band = math.ceil(math.log(2*eps*n))
        p = 2*eps*n
        for alpha in range(1, max_band+1):
            lower_bound = p-2**alpha-p%(2**alpha)
            upper_bound = p-2**(alpha-1)-p%(2**(alpha-1))
            if self.delta > lower_bound and self.delta <= upper_bound:
                return alpha
            if self.delta == p:
                return 0
        return max_band+1