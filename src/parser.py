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


if __name__ == "__main__":
    main()
