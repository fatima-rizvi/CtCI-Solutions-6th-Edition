class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class ListNode():
  def __init__(self, value =None, next=None):
    self.value, self.next = value, next
  
  def __str__(self):
    return str(self.value) + ',' + str(self.next)

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
    item = self.head.value
    self.head = self.head.next
    return item

