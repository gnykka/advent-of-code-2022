print("12a.py")
print("------")

file = open("data/12.txt", "r")
data = file.read().split("\n")

start = {}
end = {}

grid = []


# create the grid as for the maze
for i, r in enumerate(data):
  if "S" in r: start = { "row": i, "col": r.index("S") }
  if "E" in r: end = { "row": i, "col": r.index("E") }

  row = list(r.replace("S", "a").replace("E", "z"))

  for j, c in enumerate(row):
    row[j] = { "row": i, "col": j, "height": ord(c), "distance": None }

  grid.append(row)

# create the maze
# links are the possible routes from each cell
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

# dijkstra's algorithm to calculate shortest paths
def calculate_distances(cell):
  grid[cell["row"]][cell["col"]]["distance"] = 0

  frontier = [cell]

  while len(frontier) > 0:
    new_frontier = []

    for item in frontier:
      cell = grid[item["row"]][item["col"]]

      for link in cell["links"]:
        if grid[link["row"]][link["col"]]["distance"] == None:
          grid[link["row"]][link["col"]]["distance"] = cell["distance"] + 1
          new_frontier.append(link)

    frontier = new_frontier

calculate_distances(start)

print(grid[end["row"]][end["col"]]["distance"])
