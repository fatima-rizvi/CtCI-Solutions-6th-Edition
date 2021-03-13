# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list
# (You are not allowed to cheat and just convert the linked list into an integer)

from utils import LinkedList

# List visual: [7, 1, 6]
list_1 = LinkedList()
list_1.add_to_tail(7)
list_1.add_to_tail(1)
list_1.add_to_tail(6)

# List visual: [5, 9, 2]
list_2 = LinkedList()
list_2.add_to_tail(5)
list_2.add_to_tail(9)
list_2.add_to_tail(2)

# List visual: [4, 0, 9, 3]
list_3 = LinkedList()
list_3.add_to_tail(4)
list_3.add_to_tail(0)
list_3.add_to_tail(9)
list_3.add_to_tail(3)

# List visual: [2, 7, 8]
list_4 = LinkedList()
list_4.add_to_tail(2)
list_4.add_to_tail(7)
list_4.add_to_tail(8)

def sum_lists(ll1, ll2):
  res = LinkedList()

  cursor1 = ll1.head
  cursor2 = ll2.head

  carry = False
  while cursor1 or cursor2:
    val_sum = 0

    if cursor1:
      val_sum += cursor1.value
      cursor1 = cursor1.next
      
    if cursor2:
      val_sum += cursor2.value
      cursor2 = cursor2.next

    if carry:
      val_sum += 1

    if val_sum > 9:
      carry = True
      val_sum -= 10
    else:
      carry = False
  
    res.add_to_tail(val_sum)

  res.print_list()
  return res

sum_lists(list_1, list_2) # Res: [2, 1, 9]
sum_lists(list_3, list_4) # Res: [6, 7, 7, 4]
