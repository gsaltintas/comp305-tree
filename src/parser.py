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

def dp_solution(tree, dfs,child_count,k):
    node_count=tree.node_no
    total=[0]*(node_count)
    for i in range(node_count):
        if i==0:
            total[i]=int(dfs[i].weight)
        else:
            total[i]=int(dfs[i].weight) +total[i-1]
    
    result = [0]*(node_count)
    for j in range(node_count):
        result[j]=total[j]
    
    for k in range(k):
        for n in reversed(range(0,node_count)):
            pos = n +child_count[n]-1
            if n!=0: 
                result[pos] =max (result[pos],result[n-1])
        
        for k in range(node_count):
            if k==0:
                result[k]= max(result[k],int(dfs[k].weight))
            else:
                result[k]=max(result[k],result[k-1]+int(dfs[k].weight))

    print(result[node_count-1])

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
