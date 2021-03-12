# Implement an algorithm to delete a node in the middle (not neccessarily the middle, just not the head or tail) of a singly linked list, given only access to that node.

from utils import LinkedList

# List visual: [1, 2, 3, 4, 5, 6, 7, 8, 9]
linked_list = LinkedList()
linked_list.add_to_tail(1)
linked_list.add_to_tail(2)
linked_list.add_to_tail(3)
linked_list.add_to_tail(4)
linked_list.add_to_tail(5)
linked_list.add_to_tail(6)
linked_list.add_to_tail(7)
linked_list.add_to_tail(8)
linked_list.add_to_tail(9)

def delete_middle_node(node):
  node.value = node.next.value
  node.next = node.next.next

delete_middle_node(linked_list.head.next.next) #Removes node 3
linked_list.print_list()  # Check linked list

