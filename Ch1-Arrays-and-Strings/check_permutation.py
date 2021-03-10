# Given two strings, check if one is a permutation of the other

def check_permutation(str1, str2):
  freq1 = {}
  freq2 = {}

  for char in str1:
    if freq1.get(char):
      freq1[char] += 1
    else:
      freq1[char] = 1

  for char in str2:
    if freq2.get(char):
      freq2[char] += 1
    else:
      freq2[char] = 1

  for char, count in freq1.items():
    if freq2.get(char) != count:
      return False
  
  return True

print(check_permutation("asdfghjkl", "lkjhgfdsa"))
print(check_permutation("volleyball", "lbavloeyll"))
print(check_permutation("not", "correct"))
