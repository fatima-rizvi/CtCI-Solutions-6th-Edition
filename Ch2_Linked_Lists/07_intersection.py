from utils import Node

# Setting up the linked lists
inter_node = Node(5)
first_node = Node(1)
second_node = Node(7)
third_node = Node(4)

# Visual: [1, 5, 7, 4]
first_node.next = inter_node
inter_node.next = second_node
second_node.next = third_node


fourth_node = Node(2)
fifth_node = Node(9)
sixth_node = Node(3)

# Visual: [2, 9, 3, 5]
fourth_node.next = fifth_node
fifth_node.next = sixth_node
sixth_node.next = inter_node



def intersection(head1, head2):
  cursor1 = head1

  while cursor1:
    cursor2 = head2
    while cursor2:
      if cursor1 == cursor2:
        print(f"Intersecting node value: {cursor1.value}")
        return cursor1
      cursor2 = cursor2.next
    cursor1 = cursor1.next


print(intersection(first_node, fourth_node))
