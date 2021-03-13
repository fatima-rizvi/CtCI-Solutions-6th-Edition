# Write a function to check if a linked list is a palindrome

from utils import LinkedList

# List visual: [r, a, c, e, c, a, r]
a_palindrome = LinkedList()
a_palindrome.add_to_tail("r")
a_palindrome.add_to_tail("a")
a_palindrome.add_to_tail("c")
a_palindrome.add_to_tail("e")
a_palindrome.add_to_tail("c")
a_palindrome.add_to_tail("a")
a_palindrome.add_to_tail("r")

# List visual: [c, o, a, c, h]
not_a_palindrome = LinkedList()
not_a_palindrome.add_to_tail("c")
not_a_palindrome.add_to_tail("o")
not_a_palindrome.add_to_tail("a")
not_a_palindrome.add_to_tail("c")
not_a_palindrome.add_to_tail("h")

def palindrome_check(ll):
  ll.print_list()
  ahead = behind = ll.head
  stack = []

  while ahead and ahead.next:
      stack.append(behind.value)
      # print(f"Stack: {stack}\nahead: {ahead.value}\nbehind: {behind.value}\n--------")
      behind = behind.next
      ahead = ahead.next.next

  if ahead:
      behind = behind.next


  while behind:
      top = stack.pop()

      # print(f"Top: {top} Behind: {behind.value}")
      if top != behind.value:
          return False

      behind = behind.next

  return True



print(palindrome_check(a_palindrome))
print(palindrome_check(not_a_palindrome))
