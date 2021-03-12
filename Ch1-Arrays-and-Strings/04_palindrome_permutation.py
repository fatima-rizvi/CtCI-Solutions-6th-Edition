# Given a string, write a function to check if it is a permutation of a palindrome

def palindrome_permutation(str1):
  str1 = str1.replace(" ", "")
  count = {}

  for char in str1:
    if count.get(char):
      count[char] += 1
    else:
      count[char] = 1

  odds = 0
  for char, num in count.items():
    if num % 2 != 0:
      odds += 1

  if odds > 1:
    return False
  return True

print(palindrome_permutation("tact coa"))   # True, taco cat
print(palindrome_permutation("cacr ear"))   # True, race car
print(palindrome_permutation("livo veile")) # True, evil olive
print(palindrome_permutation("not one"))    # False
