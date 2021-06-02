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
- [ ] Basic Greedy algorithm (Necla)
    - Do DFS on tree
    - Cut the most-negative valued subtree, update total value of the tree
    - Keep track of the number of cuts, return when $c\geq k$ or all subtree values >= 0
- [ ] Dynamic programming approach (Yağmur)
- [ ] Test cases (at least 3 for each person)
- [ ] Presentation & Explanation & Compilation of all appraoches (Enes)

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

# Meetings
| #  | Date  | Explanation |
| -- | ----  | ----------  |
| 1  |  May 12, 2021 | Initial meeting, planning |
| 4  |  May 29, 2021 | Finalize & Task distribution |