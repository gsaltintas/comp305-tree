import argparse
import os
import time

from src.Tree import Tree, Vertex, Edge
from src.algorithms import Algorithms


def test_approach(approach: str, sample_no: int, func, args: tuple) -> str:
    """ For a given Sample #sample_no evaluates an approach by running func with provided args and logs run time """
    res = f"{approach.capitalize()} Programming Approach for the Example #{sample_no}\n"
    start = time.time()+1
    soln = func(*args)
    time.sleep(1)
    res += '%d\nTotal run time %.5f\n' % (
        soln, time.time()-start)
    return res


def main(args):
    algorithms = Algorithms()
    src_dir = os.path.dirname(os.path.realpath(__file__))
    files_len = len(os.listdir(os.path.join(src_dir, "..", "resources")))
    for sample_no in range(1, files_len+1):
        f = os.path.join(src_dir, "..", "resources", "tree%d.txt" % sample_no)
        output_f = os.path.join(src_dir, "..", "output",
                                "tree%d.txt" % sample_no)
        with open(output_f, "w") as file:
            tree, k = parse_data(f)
            visited = []
            count = []
            (visited, count) = tree.dfs_order()
            result_str = f"{'-'*15}\nEvaluating Test Case #{sample_no}\tn={tree.node_no}, k={k}\n"

            if args.dp:
                result_str += test_approach('dynamic', sample_no,
                                            algorithms.dp_solution, (visited, count, 1, k, tree.node_no))

            if args.greedy:
                result_str += test_approach('greedy', sample_no,
                                            algorithms.greedy_solution, (tree, k))
            print(result_str)
            file.write(result_str)


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
