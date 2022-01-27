'''
Read 
    - DFS: in/pre/post traversal - Time O(n) | Space O(h), h is max height (recusrsion stack)
    - BFS: level order traversal - Time O(n) | Space O(w), w is max width of any level 

Extra space required for Level order traversal is likely to be more when tree is more balanced 
and extra space for Depth First Traversal is likely to be more when tree is less balanced

How to choose DFS or BFS for use?

1. Extra Space can be one factor (Explained above)
2. Depth First Traversals are typically recursive and recursive code requires function call overheads.
3. The most important points is, BFS starts visiting nodes from root while DFS starts visiting 
nodes from leaves. So if our problem is to search something that is more likely to closer to 
root, we would prefer BFS. And if the target node is close to a leaf, we would prefer DFS.
'''
