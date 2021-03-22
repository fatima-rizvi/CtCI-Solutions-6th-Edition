# Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

from utils import Node

def is_balanced(node):
  if node.left and node.right:
    return is_balanced(node.left) and is_balanced(node.right)

  if node.left:  # Only the left node exists
    # If this node has a child
    if node.left.left or node.left.right:
        return False  # two layers, unbalanced

  if node.right:  # Only the right node exists
    # If this node has a child
    if node.right.left or node.right.right:
        return False

  return True

node_dd = Node('DD')
node_d = Node('D')
node_ccc = Node('CCC')
node_cc = Node('CC', node_dd)
node_c = Node('C', node_d)
node_bb = Node('BB', None, node_ccc)
node_b = Node('B', node_c, node_cc)
node_a = Node('A', node_b, node_bb)

node_z = Node('Z')
node_yy = Node('YY')
node_y = Node('Y', node_z)
node_xx = Node('XX', None, node_yy)
node_x = Node('X', node_y)
node_w = Node('W', node_x, node_xx)

print(is_balanced(node_a))  # Balanced: True
print(is_balanced(node_w))  # Balanced: False
