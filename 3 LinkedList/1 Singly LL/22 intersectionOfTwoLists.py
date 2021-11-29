'''
Question: There are two singly linked lists in a system. 
By some programming error, the end node of one of the 
linked list got linked to the second list, forming an 
inverted Y shaped list. Write a program to get the point 
where two linked list merge.

Use address to compare.

Approach 1: Two forloops Time O(M*N)

Approach 2: HashTable Time(N) | Space (N)
If same node visited again.

Approach 3: find length Time O(N)
Find diff of len of two lists, say d1.
start from dth node for longesr list
and start from firstNode in shorter list.
Now compare each node while traversal,
if same.
'''
