print("08a.py")
print("------")

file = open("data/08.txt", "r")
data = file.read()

tree_rows = data.split("\n")

count = 0

for i, row in enumerate(tree_rows):
  for j, tree in enumerate(row):
    if i == 0 or i == len(tree_rows) - 1 or j == 0 or j == len(row) - 1:
      count += 1
    elif (
      not any(t >= tree for t in row[0:j]) or
      not any(t >= tree for t in row[j + 1:]) or
      not any(t >= tree for t in map(lambda r: r[j], tree_rows[0:i])) or
      not any(t >= tree for t in map(lambda r: r[j], tree_rows[i + 1:]))
    ):
      count += 1

print(count)
