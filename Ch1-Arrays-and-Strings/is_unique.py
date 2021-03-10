# Determine if a string has all unique characters

# Solution implemented with a dictionary
def is_unique_with_dict(str):
  frequency = {}
  
  for char in str:
    if frequency.get(char):
      return False
    frequency[char] = 1
    
  return True
  
# Solution implemented with a list
def is_unique(str):
  chars = []

  for char in str:
    if char in chars:
      return False
    else:
      chars.append(char)
  
  return True

print(is_unique_with_dict("aassddfgg"))
print(is_unique_with_dict("asdfghjkl"))
print(is_unique_with_dict("thelazyfox"))

print(is_unique("aassddfgg"))
print(is_unique("asdfghjkl"))
print(is_unique("thelazyfox"))
