import argparse
import os

from src.Tree import Tree, Vertex, Edge
from src.algorithms import dp_solution, greedy_solution, find_subtree_sums


def main(args):
    src_dir = os.path.dirname(os.path.realpath(__file__))
    files_len = len(os.listdir(os.path.join(src_dir, "..", "resources")))
    for sample_no in range(1, files_len+1):
        f = os.path.join(src_dir, "..", "resources", "tree%d.txt" % sample_no)
        tree, k = parse_data(f)
        # print(f"For the example #{sample_no}, tree:\n{tree}")
        visited = []
        count = []
        (visited, count) = tree.dfs_order()
        print(f"{'-'*15}\nEvaluating Test Case #{sample_no}\tn={tree.node_no}, k={k}")
        if args.dp:
            print(f"Dynamic Programming Approach for the Example #{sample_no}")
            dp_solution(tree, visited, count, k)
        if args.greedy:
            print(f"Greedy Approach for the Example #{sample_no}")
            greedy_solution(tree, k)
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


def get_arguments():
    parser = argparse.ArgumentParser(
        description="The most valuable tree source code")
    parser.add_argument(
        '-d', '--dp', help='Specify to run Dynamic Programming approach', action="store_true")
    parser.add_argument(
        '-g', '--greedy', help='Specify to Greedy approach', action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    main(get_arguments())
