'''
We are given a matrix that contains different values in each cell. Our aim is to find the minimal set of positions in the matrix such that the entire matrix can be traversed starting from the positions in the set. 
We can traverse the matrix under the below conditions: 

We can move only to those neighbors that contain values less than or equal to the current cell’s value. A neighbor of the cell is defined as the cell that shares a side with the given cell.

Input : 1 2 3
        2 3 1
        1 1 1

s1. create array called results 
s2. add highest value in matrix to array
s3. visit all nodes (DFS) starting from this 
highest value
s4. from the unvisited nodes, add the highest 
value to results array 
s4. s3
s5. s4
s6. keep repeating until all nodes visited
'''
