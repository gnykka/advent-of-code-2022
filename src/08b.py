print("08b.py")
print("------")

file = open("data/08.txt", "r")
data = file.read()

tree_rows = data.split("\n")

max_score = 0

def find_distance(tree, lst):
  for i, t in enumerate(lst):
    if tree <= t: return i + 1
  return len(lst)

for i, row in enumerate(tree_rows):
  for j, tree in enumerate(row):
    if i == 0 or i == len(tree_rows) - 1 or j == 0 or j == len(row) - 1: continue

    to_left = row[0:j][::-1]
    to_right = row[j + 1:]
    to_top = list(map(lambda r: r[j], tree_rows[0:i]))[::-1]
    to_bottom = list(map(lambda r: r[j], tree_rows[i + 1:]))

    score = (
      find_distance(tree, to_left) * find_distance(tree, to_right) *
      find_distance(tree, to_top) * find_distance(tree, to_bottom)
    )

    max_score = max(max_score, score)

print(max_score)
