class Node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None
        
class ListNode():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self.data) + ',' + str(self.next)

class Queue():
  def __init__(self):
    self.head, self.tail = None, None
  
  def add(self, item):
    if self.head:
      self.tail.next = ListNode(item)
      self.tail = self.tail.next
    else:
      self.head = self.tail = ListNode(item)
  
  def remove(self):
    if not self.head:
      return None
    item = self.head.data
    self.head = self.head.next
    return item

