# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
# Note: Not necessarily a binary search tree.

from utils import Node

def first_common_ancestor(root, p, q):
  # If either of the nodes are not in the same tree
  if not is_parent(root, p) or not is_parent(root, q):
    return None
  
  #If they are in the same tree
  # Run the helper function to find the common ancestor
  return find_ancestor(root, p, q)

def is_parent(root, node):
  if root is None:  # Check to see if the root exists
    return False
  if root == node:  # Check if the node is in the tree
    return True
  # Traverse the rest of the tree to find the NotImplementedError
  return is_parent(root.left, node) or is_parent(root.right, node)

def find_ancestor(root, p, q):
  # If there is no root, or if the root is one of the two nodes
  # being searched for, return the root
  if not root or root == p or root == q:
    return root

  # Check to see whether or not each node is on the left of the tree
  p_onleft = is_parent(root.left, p)
  q_onleft = is_parent(root.left, q)

  # If both nodes are not on the same side of the tree
  # return the root as the first common ancestor
  if p_onleft is not q_onleft:
        return root

  # If both nodes are on the left, recurse on the left side
  if p_onleft and q_onleft:
    return find_ancestor(root.left, p, q)
  # If both nodes are on the right, recurse on the right side
  else:
    return find_ancestor(root.right, p, q)
  
# First Binary Search Tree
node_i = Node(13)
node_h = Node(4)
node_g = Node(7)
node_f = Node(14, node_i)
node_e = Node(6, node_h, node_g)
node_d = Node(1)
node_c = Node(10, None, node_f)
node_b = Node(3, node_d, node_e)
node_a = Node(8, node_b, node_c)

# Second Binary Search Tree
node_w = Node(14)
node_v = Node(6)
node_u = Node(1)
node_t = Node(10, None, node_w)
node_s = Node(3, node_u, node_v)
node_r = Node(8, node_s, node_t)

# print(first_common_ancestor(node_b, node_h, node_g))

res1= first_common_ancestor(node_a, node_b, node_c)
print(res1.value) # Expected: node_a, value: 8
res2 = first_common_ancestor(node_a, node_h, node_g)
print(res2.value) # Expected: node_e, value: 6
res3 = first_common_ancestor(node_a, node_i, node_e)
print(res3.value) # Expected: node_a, value: 8
res4 = first_common_ancestor(node_a, node_c, node_t)
print(res4) # Expected: False, no common ancestor
