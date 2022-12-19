print("09a.py")
print("------")

file = open("data/09.txt", "r")
data = file.read()

motions = data.split("\n")

head = { "x": 4, "y": 0 }
tail = { "x": 4, "y": 0 }

positions = [
  f"{int(tail['x'])}_{int(tail['y'])}"
]

def get_next(position, direction):
  if direction == "D":
    return { "x": position["x"] + 1, "y": position["y"] }
  if direction == "U":
    return { "x": position["x"] - 1, "y": position["y"] }
  if direction == "L":
    return { "x": position["x"], "y": position["y"] - 1 }
  if direction == "R":
    return { "x": position["x"], "y": position["y"] + 1 }

def are_neighbours(p1, p2):
  if abs(p1["x"] - p2["x"]) <= 1 and abs(p1["y"] - p2["y"]) <= 1:
    return True
  return False

for motion in motions:
  [direction, count] = motion.split(" ")

  for i in range(int(count)):
    prev_head = head
    head = get_next(head, direction)

    neighbouring = are_neighbours(head, tail)

    # trick: tail is always at the head's previous position
    if not neighbouring:
      tail = prev_head
      tail_str = f"{int(tail['x'])}_{int(tail['y'])}"
      if not tail_str in positions: positions.append(tail_str)

print(len(positions))
