print("12b.py")
print("------")

file = open("data/12.txt", "r")
data = file.read().split("\n")

end = {}
grid = []

for i, r in enumerate(data):
  if "E" in r: end = { "row": i, "col": r.index("E") }

  row = list(r.replace("S", "a").replace("E", "z"))

  for j, c in enumerate(row):
    row[j] = { "row": i, "col": j, "height": ord(c), "distance": None }

  grid.append(row)

for i, row in enumerate(grid):
  for j, cell in enumerate(row):
    height = cell["height"]
    links = []

    if i > 0 and grid[i - 1][j]["height"] - height <= 1:
      links.append({ "row": i - 1, "col": j })

    if i < len(grid) - 1 and grid[i + 1][j]["height"] - height <= 1:
      links.append({ "row": i + 1, "col": j })

    if j > 0 and grid[i][j - 1]["height"] - height <= 1:
      links.append({ "row": i, "col": j - 1 })

    if j < len(row) - 1 and grid[i][j + 1]["height"] - height <= 1:
      links.append({ "row": i, "col": j + 1 })

    cell["links"] = links


def calculate_distances(i, j):
  for row in grid:
    for cell in row:
      cell["distance"] = None

  grid[i][j]["distance"] = 0

  frontier = [{ "row": i, "col": j }]

  while len(frontier) > 0:
    new_frontier = []

    for item in frontier:
      cell = grid[item["row"]][item["col"]]

      for link in cell["links"]:
        if grid[link["row"]][link["col"]]["distance"] == None:
          grid[link["row"]][link["col"]]["distance"] = cell["distance"] + 1
          new_frontier.append(link)

    frontier = new_frontier


distances = []

# calculate a path from each "a" cell
for row in grid:
  for cell in row:
    if cell["height"] == ord("a"):
      calculate_distances(cell["row"], cell["col"])
      distance = grid[end["row"]][end["col"]]["distance"]
      if not distance is None: distances.append(distance)

print(min(distances))