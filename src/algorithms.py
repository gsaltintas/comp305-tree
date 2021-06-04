class Algorithms:

    def __init__(self):
        self.dfs = None
        self.child_count = None
        self.n = None
        self.dp_array = None

    def dp_recurse(self, i,k):
        # base cases
        if (i >= self.n):
            return 0
        if (k < 0):
            return float("-inf")


        # if problem has been solved before, just return it. Checking if solved by first setting everything to -0.1
        # which can no longer be the result as all nodes have integer values.
        if (self.dp_array[i][k] != -0.1):
            return self.dp_array[i][k]

        # first find the value if the segment starting at i'th vertex is not removed
        self.dp_array[i][k] = int(self.dfs[i].weight) + self.dp_recurse(i+1, k)

        if k == 0:
            return self.dp_array[i][k]
        # then get the maximum of no-cut or cut.
        # cut is calculated by 
        self.dp_array[i][k] = max(self.dp_array[i][k], self.dp_recurse(
            i+self.child_count[i], k-1))

        return self.dp_array[i][k]


    def dp_solution(self, dfs, child_count, i, k, n):
        # max values as defined in the problem
        self.dfs = dfs
        self.child_count = child_count
        self.n = n

        # initializing the memoization buffer for dynamic programming. 
        self.dp_array = [[-0.1 for _ in range(k+1)] for _ in range(n)]

        result = self.dp_recurse(i,k) + int(self.dfs[0].weight)
        print(result)
        return result



    def greedy_solution(self, tree, k):
        #tree, k = parse_data("resources/tree2.txt")

        # get dfs_order of tree, list of number of nodes in each
        # subtree rooted at each vertex
        dfs_order, counts = tree.dfs_order()
        weights = [int(v.weight) for v in dfs_order]
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
            weights = [int(v.weight) for v in dfs_order]
            sums = find_subtree_sums(weights, counts)
            k -= 1
        # at the end weights will include the remaining nodes weights
        print(sum(weights))

    # an helper function to calculate subtree sums


    def find_subtree_sums(weights, counts):
        sums = list()
        for i in range(len(weights)):
            sums.append(sum(weights[i: i + counts[i]]))
        return sums
