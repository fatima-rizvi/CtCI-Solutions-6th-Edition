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
