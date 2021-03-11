# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees.
# Try to do this in place

def rotate_matrix(m):
  for row in m:
    print(row)
  print()

  for i in range(len(m)):
    for j in range(i + 1, len(m)):
      #Switch row and column
      m[i][j], m[j][i] = m[j][i], m[i][j]
  
  for row in m:
    print(row)
  print()

  # Reverse the rows
  for i in range(len(m)):
    for j in range(len(m) //2):
      m[i][j], m[i][len(m[i]) - j - 1] = m[i][len(m[i]) - j - 1], m[i][j]

  for row in matrix:
    print(row)

rotateM([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
