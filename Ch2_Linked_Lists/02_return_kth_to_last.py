# Implement an algorithm to find the kth to last element of a singl linked list

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

def find_kth_to_last(ll, k):
  ll_list = []
  cursor = ll.head
  list_length = 0

  while cursor:
    # ll_list.append(cursor.val)
    list_length += 1
    cursor = cursor.next

  element_num = list_length - k + 1

  cursor = ll.head
  tracker = 1
  while cursor:
    if tracker == element_num:
      return cursor.value # Can just return cursor if the whole node is desired
    else:
      tracker += 1
      cursor = cursor.next

print(find_kth_to_last(linked_list, 3)) # Returns 1
print(find_kth_to_last(linked_list, 4)) # Returns 8
print(find_kth_to_last(linked_list, 7)) # Returns 3
print(find_kth_to_last(linked_list, 1)) # Returns 9
print(find_kth_to_last(linked_list, 8)) # Returns 2
print(find_kth_to_last(linked_list, 9)) # Returns 5


