# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

from utils import Node

def minimal_tree(arr):
    if len(arr) == 0:
        return None
    
    mid = len(arr) // 2
    
    current = Node(arr[mid])
    current.left = minimal_tree(arr[:mid])
    current.right = minimal_tree(arr[mid + 1:])
    

    return current.value # Can just print the current node as a whole


tester = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(minimal_tree(tester))
