# There are 3 types of edits that can be made on a string, insert a character, replace a character, or remove a character. 
# Check how many edits were made. Return True if the two strings are 0 to 1 edits apart.

def one_away(str1, str2):
  edits = 0
  dif = len(str1) - len(str2)

  if abs(dif) > 1:
    return False
  elif abs(dif) == 1:
    edits = 1

  c1 = 0
  c2 = 0

  while c1 < len(str1) - 1 and c2 < len(str2) - 1:
    if str1[c1] == str2[c2]:
      c1 += 1
      c2 += 1

    elif edits < 1:
      if len(str1) == len(str2):
        edits += 1
        c1 += 1
        c2 += 1
      elif len(str1) > len(str2):
        c2 += 1
      elif len(str2) > len(str1):
        c1 += 1

    else:
      return False

  return True

print(one_away("pale", "ple"))    # True
print(one_away("pales", "pale"))  # True
print(one_away("pale", "bale"))   # True
print(one_away("pale", "bake"))   # False
print(one_away("bats", "cats"))   # True
print(one_away("bats", "cat"))    # False
print(one_away("bats", "batter")) # False
