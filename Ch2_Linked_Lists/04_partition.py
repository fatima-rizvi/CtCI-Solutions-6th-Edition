# Write code to partition a linked list around a value x, such that all nodes less than x comes before all nodes greater than or equal to x. NOTE: The partition element x can be anywhere in the "right" partition; it does not need to appear between the left and right partition

from utils import LinkedList

# List visual: [3, 5, 8, 5, 10, 2, 1]
linked_list = LinkedList()
linked_list.add_to_tail(3)
linked_list.add_to_tail(5)
linked_list.add_to_tail(8)
linked_list.add_to_tail(5)
linked_list.add_to_tail(10)
linked_list.add_to_tail(2)
linked_list.add_to_tail(1)

def partition(ll, part):
  cursor = ll.head

  while cursor.next:
    if cursor.value >= part:
      ll.add_to_tail(cursor.value)
      if ll.head == cursor:
        ll.head = cursor.next
      cursor.value = cursor.next.value
      cursor.next = cursor.next.next
    cursor = cursor.next

  ll.print_list()

partition(linked_list, 5)
# Result: [3, 8, 10, 2, 1, 5, 5]
