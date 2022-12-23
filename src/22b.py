import re
import time
import copy

print("22b.py")
print("------")

file = open("data/22.txt", "r")
data = file.read().split("\n\n")

grid = []
for row in data[0].split("\n"):
  chars = [c for c in row]
  grid.append(chars)

size = 50

commands = re.findall(r"[0-9]+|R|L", data[1])

position = { "row": 0, "col": size }
direction = "R"

def rotate_direction(direction, rotation):
  if direction == "R": return "D" if rotation == "R" else "T"
  if direction == "D": return "L" if rotation == "R" else "R"
  if direction == "L": return "T" if rotation == "R" else "D"
  if direction == "T": return "R" if rotation == "R" else "L"

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
          next_row = row
          next_col = col
          next_direction = direction

          if row < size:
            next_row = size * 3 - 1 - row
            next_col = size * 2 - 1
            next_direction = "L"
          elif row < size * 2:
            next_row = size - 1
            next_col = size + row
            next_direction = "T"
          elif row < size * 3:
            next_row = size * 3 - 1 - row
            next_col = size * 3 - 1
            next_direction = "L"
          else:
            next_row = size * 3 - 1
            next_col = row - size * 2
            next_direction = "T"

          if grid[next_row][next_col] == "|":
            position["col"] -= 1
            break
          else:
            position["row"] = next_row
            position["col"] = next_col
            direction = next_direction

        # reached the wall
        elif grid[position["row"]][position["col"]] == "|":
          position["col"] -= 1
          break

      elif direction == "L":
        position["col"] -= 1

        row = position["row"]
        col = position["col"]

        # reached the start of the row
        if col == -1 or grid[row][col] == " ":
          next_row = row
          next_col = col
          next_direction = direction

          if row < size:
            next_row = size * 3 - 1 - row
            next_col = 0
            next_direction = "R"
          elif row < size * 2:
            next_row = size * 2
            next_col = row - size
            next_direction = "D"
          elif row < size * 3:
            next_row = size * 3 - 1 - row
            next_col = size
            next_direction = "R"
          else:
            next_row = 0
            next_col = row - size * 2
            next_direction = "D"

          if grid[next_row][next_col] == "|":
            position["col"] += 1
            break
          else:
            position["row"] = next_row
            position["col"] = next_col
            direction = next_direction

        # reached the wall
        elif grid[position["row"]][position["col"]] == "|":
          position["col"] += 1
          break

      elif direction == "D":
        position["row"] += 1

        row = position["row"]
        col = position["col"]

        # reached the end of the column
        if row == len(grid) or grid[row][col] == " ":
          next_row = row
          next_col = col
          next_direction = direction

          if col < size:
            next_row = 0
            next_col = size * 2 + col
            next_direction = "D"
          elif col < size * 2:
            next_row = size * 2 + col
            next_col = size - 1
            next_direction = "L"
          else:
            next_row = col - size
            next_col = size * 2 - 1
            next_direction = "L"

          if grid[next_row][next_col] == "|":
            position["row"] -= 1
            break
          else:
            position["row"] = next_row
            position["col"] = next_col
            direction = next_direction

        # reached the wall
        elif grid[position["row"]][position["col"]] == "|":
          position["row"] -= 1
          break

      elif direction == "T":
        position["row"] -= 1

        row = position["row"]
        col = position["col"]

        # reached the start of the row
        if row == -1 or grid[row][col] == " ":
          next_row = row
          next_col = col
          next_direction = direction

          if col < size:
            next_row = size + col
            next_col = size
            next_direction = "R"
          elif col < size * 2:
            next_row = size * 2 + col
            next_col = 0
            next_direction = "R"
          else:
            next_row = size * 4 - 1
            next_col = col - size * 2
            next_direction = "T"

          if grid[next_row][next_col] == "|":
            position["row"] += 1
            break
          else:
            position["row"] = next_row
            position["col"] = next_col
            direction = next_direction

        # reached the wall
        if grid[position["row"]][position["col"]] == "|":
          position["row"] += 1
          break

directions = ["R", "D", "L", "T"]
score = directions.index(direction) + 1000 * (position["row"] + 1) + 4 * (position["col"] + 1)

print("score =", score)
