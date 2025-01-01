def row_trees_count(row):
  tree_count = 0
  tree_len = len(row)
  
  if len(row) < 3:
    return 0
  
  for i in range(tree_len - 2):
    if (row[i] != row[i+1] and row[i] != row[i+2]) and (row[i + 1] != row[i + 2]):
      tree_count += 1
  
  return tree_count
    
if __name__ == '__main__':
  r1 = input().strip()
  r2 = input().strip()
  
  f1 = row_trees_count(r1)
  f2 = row_trees_count(r2)
  
  if f1 < f2:
    print("Anand")
  elif f1 > f2:
    print("Ashok")
  else:
    print("Draw")