# Write code to remove duplicates from an unsorted linked list

from utils import LinkedList

# List visual: [5, 2, 3, 7, 7, 8, 1, 2, 9]
linked_list = LinkedList()
linked_list.add_to_tail(5)
linked_list.add_to_tail(2)
linked_list.add_to_tail(3)
linked_list.add_to_tail(7)
linked_list.add_to_tail(7)
linked_list.add_to_tail(8)
linked_list.add_to_tail(1)
linked_list.add_to_tail(2)
linked_list.add_to_tail(9)

def view_linked_list(ll):
  res = []
  cursor = ll.head
  while cursor is not None:
    res.append(cursor.value)
    cursor = cursor.next
  return res

def remove_dups(ll):
  cursor = ll.head
  tracker = {}
  tracker[cursor.value] = 0

  while cursor and cursor.next:
    if tracker.get(cursor.next.value) == 0:
      cursor.next = cursor.next.next
    else:
      tracker[cursor.next.value] = 0
    cursor = cursor.next

  print(view_linked_list(ll))

  return ll.head

remove_dups(linked_list)

