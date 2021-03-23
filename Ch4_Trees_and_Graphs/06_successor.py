# Write an algorithm to find the "next" node (i.e., in order successor) of a given node in a binary search tree. 
# You may assume that each node has a link to its parent.


# Note: In order traversal goes as far down the left of a node as it can before working its way back up the the current node, then as far down the right as it can. 
def successor(target):
  if target:
    child = target.right
    # Check to see if there is a child node to the right of the given node
    if child:
      # If so, go as far down the left of the child node as possible and return that
      while child.left:
        child = child.left
      print(child.value)
      return child
    # If there is not a child node, check to see if the parent node exists
    # If the parent node exists, check that the parent node's value is greater than the target's value. That means the target was on the left of the parent 
    # node and that the target comes before the parent during in order traversal. 
    # In this case, return the parent.
    if target.parent and target.parent.value > target.value:
      print(target.parent.value)
      return target.parent
    # If that was not the case, then the target node was the furthest right node and has no successors after it during in order traversal
    return None


class BSTNode:
    def __init__(self, value = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Binary Search Tree
node_i = BSTNode(13)
node_h = BSTNode(4)
node_g = BSTNode(7)
node_f = BSTNode(14, node_i)
node_e = BSTNode(6, node_h, node_g)
node_d = BSTNode(1)
node_c = BSTNode(10, None, node_f)
node_b = BSTNode(3, node_d, node_e)
node_a = BSTNode(8, node_b, node_c)

node_b.parent = node_a
node_c.parent = node_a
node_d.parent = node_b
node_e.parent = node_b
node_f.parent = node_c
node_g.parent = node_e
node_h.parent = node_e
node_i.parent = node_f

print(successor(node_e)) # Expected result: node_g, value: 7 (child)
print()
print(successor(node_f)) # Expected result: None, rightmost node
print()
print(successor(node_d)) # Expected result: node_b, value: 3 (parent)
