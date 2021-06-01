import os
from Tree import Tree, Vertex, Edge


def main():
    sample_no = 0
    print(os.getcwd())
    for f in os.listdir(os.path.join(os.getcwd(), "..", "resources")):
        f = os.path.join("..", "resources", f)
        tree, k = parse_data(f)
        print(f"For example {sample_no}, tree:\n{tree}")
        visited = []
        count= []
        (visited,count) =tree.dfs_order()
        dp_solution(tree,visited,count,k)
       
        sample_no += 1

def dp_solution(tree, dfs_order,cnt,k):
    sum=[0]*(tree.node_no+1)
    for i in range(1,tree.node_no+1):
        sum[i]=int(dfs_order[i-1].weight) +sum[i-1]
    
    f = [0]*(tree.node_no+1)
    for j in range(1,tree.node_no+1):
        f[j]=sum[j]
    
    for k in range(1,k+1):
        for n in range(tree.node_no,0,-1):
            pos = n +cnt[n-1] -1
            f[pos] =max (f[pos],f[n-1])

        for k in range(1,tree.node_no+1):
            f[k]=max(f[k],f[k-1]+int(dfs_order[k-1].weight))

    print(f[tree.node_no])
    
def greedy_solution(tree, k):
    #tree, k = parse_data("resources/tree2.txt")   
    
    # get dfs_order of tree, list of number of nodes in each
    # subtree rooted at each vertex 
    dfs_order, counts = tree.dfs_order()
    weights  = [int(v.weight) for v in dfs_order]
    sums = find_subtree_sums(weights, counts)

    # loop until we are out of cuts or there is no node
    # left in the tree
    while k > 0 and len(weights) > 0:
        # find subtree with minimum sum
        min_sum = min(sums)
        # if minimum sum is positive don't cut anything
        if min_sum > 0:
            break
        # find the index of the node which is the root
        # of the subtree with minimum sum
        index_min = sums.index(min_sum) 
        # cut the subtree with minimum sum
        sums.remove(min_sum)
        # get number of nodes in the subtree that will be cut
        num_nodes_in_subtree = counts[index_min]
        # remove each vertex in that subtree from our tree
        for i in range(index_min, index_min + num_nodes_in_subtree):
            dfs_order[i].remove_yourself()
        # get the dfs order and number of nodes in the subtrees
        # after cutting a subtree
        dfs_order, counts = tree.dfs_order()
        # sum of the values for nodes will be zero because this 
        # part was prepared to take care of dp solution not the 
        # greedy one so we need to remove zeros for keeping 
        # consistent indices according to dfs_order
        while 0 in counts:
            counts.remove(0)
        # get new weights and subtree sums    
        weights  = [int(v.weight) for v in dfs_order]
        sums = find_subtree_sums(weights, counts)    
        k -= 1
    # at the end weights will include the remaining nodes weights   
    print(sum(weights))

# an helper function to calculate subtree sums
def find_subtree_sums(weights, counts):
    sums = list()
    for i in range(len(weights)):
        sums.append(sum(weights[i : i + counts[i]]))
    return sums

def parse_data(path: str) -> tuple:
    """
    parse data in the file specified with path and construct the tree
    :param path: path to the example tree
    :return: Tree and k, maximum cuts
    """
    with open(path, "r") as data:
        line_num = 0
        for line in data:
            line = line.strip()
            if line_num == 0:
                n, k = (int(i) for i in line.split(" "))
                tree = Tree(n)
            elif line_num == 1:
                weights = line.split(" ")
                for i in range(n):
                    v = Vertex(weights[i], i)
                    tree.add_vertex(v)
            else:
                # examples use 1-index
                v1, v2 = (int(i)-1 for i in line.split(" "))
                # tree.add_edge(Edge(v1, v2))
                tree.add_edge(v1, v2)
            line_num += 1
    return tree, k





if __name__ == "__main__":
    main()
    
    
    
        
       
