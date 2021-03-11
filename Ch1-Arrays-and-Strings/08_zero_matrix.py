# If an element in the matrix is zero, set it's whole row and column to zero

# Note: Print statements were added for visuals

def zero_matrix(m):
  for row in m:
    print(row)
  print()

  zero_rows = []
  zero_cols = []
  for i in range(len(m)):
    for j in range(len(m[i])):
      # print([i, j])
      if m[i][j] == 0:
        zero_rows.append(i)
        zero_cols.append(j)
  
  # print(zero_rows)
  # print(zero_cols)

  for row in zero_rows:
    m[row] = [0 for num in m[row]]

  for i in range(len(m)):
    for col in zero_cols:
      m[i][col] = 0
    print(m[i])

  return m




zero_matrix([
  [ 5, 1, 9,11],
  [ 2, 4, 0,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
print()
zero_matrix([
  [ 0, 1, 9,11],
  [ 2, 4, 0,10],
  [13, 3, 6, 7],
  [15, 14,12,16]
])
