# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
# (e.g., if you have a tree with depth D, you'll have D linked list)

from utils import Node, ListNode, Queue

def list_of_depths(binary_tree):
  if not binary_tree:
    return []
  lists = []
  queue = Queue()
  current_depth = -1
  current_tail = None
  node = binary_tree
  node.depth = 0  # Create a depth attribute to keep track of the node's level on the tree

  while node:
    # print(f"ND: {node.depth}, {node.value}")
    # print(f"CD: {current_depth}\n")
    if node.depth == current_depth: # Continuing on teh current level
      current_tail.next = ListNode(node.value)
      current_tail = current_tail.next
    else: # Moving onto the next level
      current_depth = node.depth
      current_tail = ListNode(node.value)
      lists.append(current_tail)
    for child in [node.left, node.right]: # Adding the child nodes to the queue
      if child:
        child.depth = node.depth + 1  # Indicating the correct depth the child nodes are on
        queue.add(child)
    node = queue.remove()
  return lists

node_dd = Node('DD')
node_d = Node('D')
node_ccc = Node('CCC')
node_cc = Node('CC', node_dd)
node_c = Node('C', node_d)
node_bb = Node('BB', None, node_ccc)
node_b = Node('B', node_c, node_cc)
node_a = Node('A', node_b, node_bb)
lists = list_of_depths(node_a)  

for ll in lists:
  current = ll
  while current:
    print(current.value) 
    current = current.next
  print()
