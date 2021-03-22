# Implement a function to check if a binary tree is a binary search tree

from utils import Node

def validate_bst(bst):
    return validate_helper(bst)

def validate_helper(node, min=None, max=None):
    if not node:  # Check to see if the node exists
        return True
    # Make sure the node value is within bounds. If not, return False
    if (min and node.value < min) or (max and node.value >= max):
        return False
    # If it is within bounds, continue traversing the tree and checking.
    return validate_helper(node.left, min, node.value) and validate_helper(
        node.right, node.value, max
    )  

# Valid Binary Search Tree
node_i = Node(13)
node_h = Node(4)
node_g = Node(7)
node_f = Node(14, node_i)
node_e = Node(6, node_h, node_g)
node_d = Node(1)
node_c = Node(10, None, node_f)
node_b = Node(3, node_d, node_e)
node_a = Node(8, node_b, node_c)

# Binary Tree, not a search tree
node_z = Node(5)
node_y = Node(7)
node_x = Node(6)
node_w = Node(2, node_z)
node_v = Node(19, node_y, node_x)
node_u = Node(1)
node_t = Node(10, None, node_w)
node_s = Node(3, node_u, node_v)
node_r = Node(9, node_s, node_t)

print(validate_bst(node_a)) # Valid: True
print(validate_bst(node_r)) # Valid: False
