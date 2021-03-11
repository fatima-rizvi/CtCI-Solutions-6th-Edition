# Implemet a method to perform basic string compression using the count of repeated characters
# If the "compressed" string is not shorter than the original string, return the original string.

def string_compression(str1):
  letters = []
  counts = []

  cursor = str1[0]
  letters.append(cursor)
  temp = 0

  for i in range(len(str1)):
    if str1[i] == cursor:
      temp += 1
      
    else:
      counts.append(temp)
      temp = 1
      cursor = str1[i]
      letters.append(cursor)

  counts.append(temp)

  res = ""
  for i in range(len(letters)):
    res += letters[i]
    res += str(counts[i])

  if len(str1) < len(res):
    return str1
  return res

print(string_compression("aabcccccaaa")) # a2b1c5a3
