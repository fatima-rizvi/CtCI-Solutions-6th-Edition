# Write a method to replace all spaces in a string with '%20'

def urlify(str1, true_len):
  res = ""
  str1 = str1.strip()

  for char in str1:
    if char == " ":
      res += "%20"
    else:
      res += char

  return res

print(urlify("Mr John Smith    ", 13))
