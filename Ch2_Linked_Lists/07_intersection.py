from utils import Node

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

fourth_node = Node(4)
fifth_node = Node(5)
sixth_node = Node(6)

eighth_node = Node(8)
ninth_node = Node(9)
tenth_node = Node(10)
eleventh_node = Node(11)

# Visuals
# [1, 2, 3, 8, 9, 10, 11]
# [4, 5, 6, 8, 9, 10, 11]

first_node.next = second_node
second_node.next = third_node
third_node.next = eighth_node

fourth_node.next = fifth_node
fifth_node.next = sixth_node
sixth_node.next = eighth_node

eighth_node.next = ninth_node
ninth_node.next = tenth_node
tenth_node.next = eleventh_node

def intersection(head1, head2):
  # Check to see if both nodes end in the same place
  # Track list length
  length1 = 0
  length2 = 0

  cursor1 = head1
  while cursor1:
    cursor1 = cursor1.next
    length1 += 1
  
  cursor2 = head2
  while cursor2:
    cursor2 = cursor2.next
    length2 += 1

  if cursor1 != cursor2:
    return False

  len_dif = length1 - length2

  if len_dif > 0:
    long_node = head1
    short_node = head2
  else:
    long_node = head2
    short_node = head1
    len_dif *= -1

  for i in range(len_dif):
    long_node = long_node.next

  while long_node:
    long_node = long_node.next
    short_node = short_node.next
    if long_node == short_node:
      print(f"Intersecting node value: {long_node.value}")
      return long_node

  return False

print(intersection(first_node, fourth_node))
