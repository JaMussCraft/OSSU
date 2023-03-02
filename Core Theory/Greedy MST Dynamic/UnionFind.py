class UnionFind():
    def __init__(self, num_of_nodes):
        # takes in node and return its leader 
        self.leaders = [i for i in range(num_of_nodes+1)]
        # takes in leader and return every node under that leader
        # leader to list of nodes under that leader
        # 5: [3,8,6,3]
        self.clusters = {i: [i] for i in range(1, num_of_nodes+1)}
        # takes in leader and return the number of nodes under it
        self.cluster_size = [1 for i in range(num_of_nodes+1)]

    def find(self, node):
        return self.leaders[node]

    def union(self, node_1, node_2):
        leader_node_1 = self.leaders[node_1]
        leader_node_2 = self.leaders[node_2]

        if leader_node_1 == leader_node_2:
            print('Already in the same cluster')
            return

        size_leader_1 = self.cluster_size[leader_node_1]
        size_leader_2 = self.cluster_size[leader_node_2]



        # size of both leaders are the same
        if size_leader_1 == size_leader_2:
            # it does not matter which one to rewire
            # rewire every node under leader 1 to leader 2
            for node in self.clusters[leader_node_1]:
                # add the node to the cluster of leader 2
                self.clusters[leader_node_2].append(node)
                self.leaders[node] = leader_node_2
            
                # increase the cluster size of leader 2
                self.cluster_size[leader_node_2] += 1

            # delete the cluster of leader 1
            del self.clusters[leader_node_1]


        # size of leader 1 is bigger
        elif size_leader_1 > size_leader_2:
            # rewire every node under leader 2 to leader 1
            for node in self.clusters[leader_node_2]:
                # add the node to the cluster of leader 1
                self.clusters[leader_node_1].append(node)
                self.leaders[node] = leader_node_1
            
                # increase the cluster size of leader 1
                self.cluster_size[leader_node_1] += 1

            # delete the cluster of leader 2
            del self.clusters[leader_node_2]

        else: # size of leader 2 is bigger
            # rewire every node under leader 1 to leader 2
            for node in self.clusters[leader_node_1]:
                # add the node to the cluster of leader 2
                self.clusters[leader_node_2].append(node)
                self.leaders[node] = leader_node_2
            
                # increase the cluster size of leader 2
                self.cluster_size[leader_node_2] += 1

            # delete the cluster of leader 1
            del self.clusters[leader_node_1]


    def get_clusters(self):
        return self.clusters
    
    def get_num_clusters(self):
        return len(self.clusters)



if __name__ == '__main__':
    num_of_nodes = 5
    union = UnionFind(num_of_nodes)
    print(union.get_clusters())
    union.union(2,3)
    print(union.get_clusters())
    union.union(4,5)
    print(union.get_clusters())
    union.union(1,2)
    print(union.get_clusters())
    union.union(1,5)
    print(union.get_clusters())





        