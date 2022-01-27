'''
- DFS: io/pre/post traversal - Time O(n) | Space O(w), w is max width of any level
- BFS: level order traversal - Time O(n) | Space O(h), h is max height (recusrsion stack)

Uses
- inorder: 
    nodes in inc order in BST
    for dec order, R Root L 
- preorder:
    create a copy of the tree
    prefix expression on an expression tree
- postorder:
    to delete the tree
    postfix expression on an expression tree

For DFS (in/pre/post) 
Space complexity:
    if we don't consider, space of recursion stack:
        O(1)
    if we consider, space of recursion stack:
        - extra space = max height of tree 
        - Worst case = skewed tree 
            > max height of tree = num of nodes in tree
            > O(n) 
        - Best case = balanced tree 
            > max height of tree =  (LogN)
            > (LogN)
Time complexity:
    General formula = T(n) = T(k) + T(n – k – 1) + c
        > k = number of nodes on one side of the root
        > n – k – 1 = number of nodes on other side of the root
    Case 1: Skewed tree
        > one subtree = empty 
        > other subtree = all nodes
        T(n) = T(0) + T(n-1) + c 
        T(n) = 2T(0) + T(n-2) + 2c 
        T(n) = 3T(0) + T(n-3) + 3c
        > T(n) = Θ(n) (Theta of n) 
    Case 2: Balanced tree 
        T(n) = 2T(n/2) + c 
        T(n) = O(n)
    
'''
