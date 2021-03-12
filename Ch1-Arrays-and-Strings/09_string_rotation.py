# Assumes that we have a mehod "isSubstring" that checks if one word is a substring of another using only one call to isSubstring
def string_rotation(str1, str2):
  if len(str1) == len(str2):
    long_str1 = str1 + str1
    return isSubstring(long_str1, str2)
  return False
  
# Another solution assuming we do not have isSubstring
def alt_string_rotation(str1, str2):

  if len(str1) != len(str2):
    return False

  orig = list(str1)
  rotating = list(str1)
  goal = list(str2)
  # print(rotating)
  move_char = rotating.pop(0)
  # print(move_char)
  rotating.append(move_char)

  while rotating != orig:
    if rotating == goal:
      return True
    else:
      move_char = rotating.pop(0)
      rotating.append(move_char)
   

  return False

print(alt_string_rotation("waterbottle", "bottlewater"))  # True
print(alt_string_rotation("waterbottle", "dog"))          # False
print(alt_string_rotation("batman", "tmanba"))            # True
print(alt_string_rotation("asdfgjk", "fghjbn"))           # False
