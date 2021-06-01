import os
from Tree import Tree, Vertex, Edge


def main():
    sample_no = 0
    for f in os.listdir(os.path.join(os.getcwd(), "..", "resources")):
        f = os.path.join("..", "resources", f)
        tree, k = parse_data(f)
        print(f"For example {sample_no}, tree:\n{tree}")
        for i in tree.dfs_order():
            print(i)
        sample_no += 1


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

def find_subtree_sums(weights):
    sums = list()
    for i in range(len(weights)):
        sums.append(sum(weights[i : i + counts[i]]))
    return sums
        
if __name__ == "__main__":
    #main()
    tree, k = parse_data("resources/tree2.txt")    
    dfs_order, counts = tree.dfs_order()
    print(list(map(lambda v: v.weight, dfs_order)))
    weights  = [int(v.weight) for v in dfs_order]
    sums = find_subtree_sums(weights)

    while k > 0 and len(weights) > 0:
        print("Sums: ", sums)
        min_sum = min(sums)
        if min_sum > 0:
            break
        index_min = sums.index(min_sum) 
          
        print("min sum: ", min_sum, "index min : ", index_min, " Num nodes in subree: ", counts[index_min])
        #sumsdan min sumı silelim
        sums.remove(min_sum)
        print("Min sum: ", min_sum)
        num_nodes_in_subtree = counts[index_min]
        #for i in range(index_min, index_min + num_nodes_in_subtree):
        #    counts.pop(i)
        #    weights.pop(i)
        # o subtreeyi kaldıralım dfs orderdan ve weightlerden tekrar 
        #sumlarıhesaplayalım
        countsCpy = counts[: index_min]
        countsCpy.extend(counts[index_min + num_nodes_in_subtree : ])
        counts = countsCpy
        weightsCpy = (weights[: index_min])
        weightsCpy.extend(weights[index_min + num_nodes_in_subtree : ])
        weights = weightsCpy
        print("Counts:", counts)
        print("Weight: ", weights)
        k -= 1
        sums = find_subtree_sums(weights)
    print(sum(sums))
    
        
       
