# comp305-tree
The Most Valuable Tree - Comp 305 Term Project

# Team Members
- Yağmur Akarken
- Gül Sena Altıntaş
- Enes M. Erciyes
- Necla Mutlu

# To-dos
- [x] Implement data structures (Gül Sena)
    - [x] Dictionary & list based graph
    - [x] Input parsing
- [x] Basic Greedy algorithm (Necla)
    - Do DFS on tree
    - Cut the most-negative valued subtree, update total value of the tree
    - Keep track of the number of cuts, return when $c\geq k$ or all subtree values >= 0
- [ ] Dynamic programming approach (Yağmur & Enes)
- [ ] Test cases (at least 3 for each person) 
- [ ] Test cases re-draw
- [ ] Presentation & Explanation & Compilation of all appraoches
    - [ ] Greedy (Enes)
    - [ ] Failed Approaches (Enes)
    - [ ] DP approach (Necla)
- [ ] Update README.md

# Run
Specify the algorithms with a flag `-d` for dynamic programming approach, `-g` for greedy.
```bash
python -m src.parser -dg
```
# Explanation
## Input
*n, k <-* number of vertices, maximum cuts
*w1 ... wn <-* weights of the vertices
*v1 v2 <-* edge betweem *v1* and *v2*

## Data Structures
We implemented three basic data structures, *Graph*, *Edge*, and *Vertex*. 
### Vertex & Edge
Each vertex is specified with a weight and id, their appereance order in the input. 

**Note** that the vertices are in 1-index in the input but they are converted to 0-index in the implementation.

### Tree
Tree is an undirected graph where any two vertices are connected by exactly one path. Hence, both vertex and edge addition are $O(1)$. Vertices of the tree are stored in a list ($O(n)$ space complexity) and each vertex has an neighbors list. As there are exactly $n-1$ edges neighbors list is also linear.
## Incorrect Greedy Approach
We implemented a greedy approach that gives incorrect results in some test cases. This solution uses three things:
- an array that keeps the vertices according to their dfs order 
- an array that keeps the number of the elements in the subtrees rooted at each vertex
- an array that keeps the sums of the subtrees rooted at each vertex
While k is greater than zero in each iteration, it removes the subtree which has the most negative sum.
## Inefficient Recursive Approach
This approach works in the following way: 
- Keep the nodes in an array ordered according to their DFS order.
- Traverse the array starting from 0th index until the last index or until the k becomes 0 in a recursive manner.
- Assumption: We have a function called findMaxValue(index, k) → finds the maximum value that is possible after the node at index by making at most k cuts
- At each index, there are two options: Keep the node of remove it.
- If we decide to keep it, we need to recurse on the remaining part of the tree: (weight of current node) + findMaxValue(index + 1, k)
- If we decide to remove it, we need to recurse on the remaining part after we remove the subtree rooted at the node that we removed: findMaxValue(index + # of elements in current node’s subtree, k - 1)
- To find the maximum value possible, we need to take the maximum of those two values. 
  - max((weight of the node) + findMaxValue(index + 1, k), findMaxValue(index + # of elements in the node’s subtree, k - 1))

## DP Approach
- If we examine recursive approach, there are possible multiple branches that ends up with calling findMaxValue function with same index and k parameters. 
- For each parameter pair, regardless of how we reached this call, findMaxValue function does same operations. Therefore, it is enough to calculate the result once for each n, k pairs and memoize it so that we can use it again. (Subproblems: each different n,k pair that we call our findMaxValue function)
- There are n * k different pairs of n, k. For each pair, we only do a maximization operation, which is O(1). In total,  the complexity is O(n * k)

# Meetings
| #  | Date  | Explanation |
| -- | ----  | ----------  |
| 1  |  May 12, 2021 | Initial meeting, planning |
| 4  |  May 29, 2021 | Finalize & Task distribution |
