# Write code to remove duplicates from an unsorted linked list

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value) 
        if self.head is None:  
            self.head = new_node
            self.tail = new_node
            return
        old_head = self.head    
        self.head = new_node   
        self.head.next = old_head 

    def remove_head(self):
        if self.head is None:
            return
        data = self.head.get_value()
        self.head = self.head.next
        return data

    def remove_tail(self):
        data = self.tail.get_value()
        cursor = self.head  
        while cursor.next.next is not None:  
            cursor = cursor.next    
        self.tail = cursor   
        self.tail.next = None   
        return data


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

