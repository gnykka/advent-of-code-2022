print("09b.py")
print("------")

file = open("data/09.txt", "r")
data = file.read()

motions = data.split("\n")

head = { "x": 15, "y": 11 }
knots = []

for i in range(9):
  knots.append(head.copy())

last = len(knots) - 1

positions = [
  f"{int(knots[last]['x'])}_{int(knots[last]['y'])}"
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
    head = get_next(head, direction)

    for i, knot in enumerate(knots):
      prev_knot = head if i == 0 else knots[i - 1]
      neighbouring = are_neighbours(prev_knot, knot)

      # trick: next knot always moves in the direction of the previous one
      if not neighbouring:
        if prev_knot["x"] > knot["x"]:
          knots[i]["x"] += 1
        if prev_knot["x"] < knot["x"]:
          knots[i]["x"] -= 1

        if prev_knot["y"] > knot["y"]:
          knots[i]["y"] += 1
        if prev_knot["y"] < knot["y"]:
          knots[i]["y"] -= 1

    tail_str = f"{int(knots[last]['x'])}_{int(knots[last]['y'])}"
    if not tail_str in positions: positions.append(tail_str)


print(len(positions))
