# Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists)

from utils import Node

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

fourth_node = Node(4)
fifth_node = Node(5)
sixth_node = Node(6)

# Visual [1, 2, 3, 4, 5, 6, 4] 
# (The second four is the same as the first, hence the loop)
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node
sixth_node.next = fourth_node

def loop_detection(head):
  cursor = head

  fast = head
  slow = head

  while fast and fast.next:
    if fast is None or slow is None:
      return None
    fast = fast.next.next
    slow = slow.next
    if fast is slow:
        break

  slow = head
  while fast is not slow:
    fast = fast.next
    slow = slow.next

  print(f"Node a start of loop value: {fast.value}")
  return fast

print(loop_detection(first_node))
