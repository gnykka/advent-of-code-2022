import re
# import time
# import copy

print("22a.py")
print("------")

file = open("data/22.txt", "r")
data = file.read().split("\n\n")

grid = []
for row in data[0].split("\n"):
  chars = [c for c in row]
  grid.append(chars)

commands = re.findall(r"[0-9]+|R|L", data[1])

position = { "row": 0, "col": 50 }
direction = "R"

def rotate_direction(direction, rotation):
  if direction == "R": return "D" if rotation == "R" else "T"
  if direction == "D": return "L" if rotation == "R" else "R"
  if direction == "L": return "T" if rotation == "R" else "D"
  if direction == "T": return "R" if rotation == "R" else "L"

def find_first_in_row(row):
  return re.search(r'[^ ]', "".join(grid[row])).start()

def find_last_in_row(row):
  matches = list(re.finditer(r'[^ ]', "".join(grid[row])))
  return matches[len(matches) - 1].start()

def find_first_in_column(col):
  column = [row[col] for row in grid]
  return re.search(r'[^ ]', "".join(column)).start()

def find_last_in_column(col):
  column = [row[col] for row in grid]
  matches = list(re.finditer(r'[^ ]', "".join(column)))
  return matches[len(matches) - 1].start()

for command in commands:
  if command == "R" or command == "L":
    direction = rotate_direction(direction, command)
  else:
    count = int(command)
    for i in range(count):
      if direction == "R":
        position["col"] += 1

        row = position["row"]
        col = position["col"]

        # reached the end of the row
        if col == len(grid[row]) or grid[row][col] == " ":
          first_col = find_first_in_row(row)
          if grid[row][first_col] == "|":
            position["col"] -= 1
            break
          else: position["col"] = first_col

        # reached the wall
        if grid[row][position["col"]] == "|":
          position["col"] -= 1
          break

      if direction == "L":
        position["col"] -= 1

        row = position["row"]
        col = position["col"]

        # reached the start of the row
        if col == -1 or grid[row][col] == " ":
          last_col = find_last_in_row(row)
          if grid[row][last_col] == "|":
            position["col"] += 1
            break
          else: position["col"] = last_col

        # reached the wall
        if grid[row][position["col"]] == "|":
          position["col"] += 1
          break

      if direction == "D":
        position["row"] += 1

        row = position["row"]
        col = position["col"]

        # reached the end of the column
        if row == len(grid) or grid[row][col] == " ":
          first_row = find_first_in_column(col)
          if grid[first_row][col] == "|":
            position["row"] -= 1
            break
          else: position["row"] = first_row

        # reached the wall
        if grid[position["row"]][col] == "|":
          position["row"] -= 1
          break

      if direction == "T":
        position["row"] -= 1

        row = position["row"]
        col = position["col"]

        # reached the start of the row
        if row == -1 or grid[row][col] == " ":
          last_row = find_last_in_column(col)
          if grid[last_row][col] == "|":
            position["row"] += 1
            break
          else: position["row"] = last_row

        # reached the wall
        if grid[position["row"]][col] == "|":
          position["row"] += 1
          break

      # printing the grid (for the sample)
      # current_grid = copy.deepcopy(grid)
      # current_grid[position["row"]][position["col"]] = "*"
      # print("\033c", end="")
      # print("\n".join(map(lambda r: "".join(r), current_grid[0:50])))
      # time.sleep(0.25)

directions = ["R", "D", "L", "T"]
score = directions.index(direction) + 1000 * (position["row"] + 1) + 4 * (position["col"] + 1)

print("score =", score)
