# A binary search tree was created by traversin through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

from utils import Node

def bst_sequences(bst):
  return bst_sequences_partial([bst])
  
def bst_sequences_partial(subtrees, partial = []):
  if not len(subtrees):
    return [partial]
  sequences = []
  # Use enumerate() to get the count of the current iteration and the value of the item at the current iteration
  for index, subtree in enumerate(subtrees):
    new_partial = partial + [subtree.value]
    new_subtrees = subtrees[:index] + subtrees[index+1:]
    if subtree.left:
      new_subtrees.append(subtree.left)
    if subtree.right:
      new_subtrees.append(subtree.right)
    sequences += bst_sequences_partial(new_subtrees, new_partial)
  return sequences

# # Binary Search Tree
# node_f = Node(14)
# node_e = Node(6)
# node_d = Node(1)
# node_c = Node(10, None, node_f)
# node_b = Node(3, node_d, node_e)
# node_a = Node(8, node_b, node_c)

# Smaller Binary Search Tree
node_t = Node(10)
node_s = Node(3)
node_r = Node(8, node_s, node_t)

# print(bst_sequences(node_a))

print(bst_sequences(node_r))
# Expected result: [[8, 3, 10], [8, 10, 3]]
