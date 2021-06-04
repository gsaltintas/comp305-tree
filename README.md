# The Most Valuable Tree - Comp 305 Term Project

# :family_woman_woman_girl_boy: Group 1 - Team Members
- Yağmur Akarken
- Gül Sena Altıntaş
- Enes M. Erciyes
- Necla Mutlu

**Corresponding TA:** Amir Mohamad Akhlaghi Gharelar
# :heavy_check_mark: To-dos
- [x] Implement data structures (Gül Sena)
    - [x] Dictionary & list based graph
    - [x] Input parsing
- [x] Basic Greedy algorithm (Necla)
    - Do DFS on tree
    - Cut the most-negative valued subtree, update total value of the tree
    - Keep track of the number of cuts, return when $c\geq k$ or all subtree values >= 0
- [x] Dynamic programming approach (Yağmur & Enes)
- [x] Test cases (at least 3 for each person), Visualization (Gül sena) 
- [x] Test cases re-draw
- [x] Presentation & Explanation & Compilation of all appraoches
    - [x] Greedy (Enes)
    - [x] Failed Approaches (Enes, Yağmur)
    - [x] DP approach (Necla)
- [x] Update README.md

# :running_woman::running_man: Run
Specify the algorithms with a flag `-d` for dynamic programming approach, `-g` for greedy.
```bash
python -m src.parser -dg
```

# :pen: Output
The evaluation of the two algorithms -see [Solutions](#pushpinsolutions)- are logged to console and saved into `output/` folder.

# :school_satchel: Explanation
## :bookmark_tabs:	Input
Test cases are included in the `resources` directory, if one wishes to add an extra test case they can add `treeX.txt` to resources where X should be strictly between 1 and total number of test cases in the directory.
*n, k <-* number of vertices, maximum cuts
*w1 ... wn <-* weights of the vertices
*v1 v2 <-* edge between *v1* and *v2*

## :paperclip: Data Structures
We implemented three basic data structures, *Graph*, *Edge*, and *Vertex*. 
### :sunflower:	Vertex
- Each vertex is specified with a weight and id, their appereance order in the input. 
    **Note** that the vertices are in 1-index in the input but they are converted to 0-index in the implementation and vi- sualizations in the presentation.
- To mimmic cut behavior, each vertex 
### :ear_of_rice: Edge
Since three is an undirected graph and the edges are unweighted, an edge simply stores reference to its two vertices and adds the two vertices to each other's neighbors during creation.

### :herb: Tree
Tree is an undirected graph where any two vertices are connected by exactly one path. Hence, we don't need complex data structures to represent the tree. 
#### Complexity Analysis
- Add the vertex to the end of tree's vertices list  O(1).
- To add an edge, add both vertices in the edge to each other's neighbors list.
- The vertices of the tree are stored in a list ($O(n)$ space complexity) and each vertex has a neighbors list. 
- Since it is a tree, there are exactly $n-1$ edges. Hence the total size of neighbors lists is bounded by $O(2n)=O(n)$.
**Note:** Here we take advantage of the input format and tree structure to optimize space and time complexities of tree operations. We assume that the first vertex is the root and the order of the edges in the input represent the DFS order of the tree.

# :pushpin:	Solutions
## :chart_with_downwards_trend:	Incorrect Greedy Approach
We implemented a greedy approach that gives incorrect results in some test cases. This solution uses three things:
- an array that keeps the vertices according to their dfs order 
- an array that keeps the number of the elements in the subtrees rooted at each vertex
- an array that keeps the sums of the subtrees rooted at each vertex
While k is greater than zero in each iteration, it removes the subtree which has the most negative sum.
## :scissors: Inefficient Recursive Approach
This approach works in the following way: 
- Keep the nodes in an array ordered according to their DFS order.
- Traverse the array starting from 0th index until the last index or until k becomes 0 in a recursive manner.
- Assumption: We have a function called findMaxValue(index, k) → finds the maximum value that is possible after the node at index by making at most k cuts
- At each index, there are two options: Keep the node of remove it.
- If we decide to keep it, we need to recurse on the remaining part of the tree: (weight of current node) + findMaxValue(index + 1, k)
- If we decide to remove it, we need to recurse on the remaining part after we remove the subtree rooted at the node that we removed: findMaxValue(index + # of elements in current node’s subtree, k - 1)
- To find the maximum value possible, we need to take the maximum of those two values. 
  - max((weight of the node) + findMaxValue(index + 1, k), findMaxValue(index + # of elements in the node’s subtree, k - 1))

## :rocket: DP Approach
- If we examine recursive approach, there are possible multiple branches that ends up with calling findMaxValue function with same index and k parameters. 
- For each parameter pair, regardless of how we reached this call, findMaxValue function does same operations. Therefore, it is enough to calculate the result once for each n, k pairs and memoize it so that we can use it again. (Subproblems: each different n,k pair that we call our findMaxValue function)
- There are n * k different pairs of n, k. For each pair, we only do a maximization operation, which is O(1). In total,  the complexity is O(n * k)

# :house_with_garden:Meetings
| #  | Date  | Details |
| -- | ----  | ----------  |
| 1  |  May 12, 2021 | Initial meeting, planning |
| 2  |  May 18, 2021 | Brainstorming, greedy approach |
| 3  |  May 19, 2021 | Tried a few dynamic programming and recursive approaches |
| 4  |  May 24, 2021 | Exploring the DFS and array based DP |
| 5  |  May 29, 2021 | Finalize & Task distribution |
| 6  |  June 3, 2021 | Test implementations, presentation preparation |
| 7  |  June 4, 2021 | Presentation preparation |
| 8  |  June 5, 2021 | Final Presentation to TA |

# :bomb: Academic Honesty
This project is developed for educational purposes only.

Koç University students who are currently taking this course, see <a href="https://apdd.ku.edu.tr/en/academic-policies/student-code-of-conduct/" target="_blank">Code of Conduct</a>.