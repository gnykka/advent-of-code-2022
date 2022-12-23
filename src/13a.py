from ast import literal_eval

print("13a.py")
print("------")

file = open("data/13.txt", "r")
data = file.read().split("\n\n")

def check_order(left, right):
  if left is None: return 1
  if right is None: return -1

  if type(left) == int and type(right) == int:
    if left == right: return 0
    if left < right: return 1
    if left > right: return -1

  if type(left) == int and type(right) != int:
    return check_order([left], right)

  if type(left) != int and type(right) == int:
    return check_order(left, [right])

  if type(left) == list and type(right) == list:
    for idx in range(max(len(left), len(right))):
      l = left[idx] if idx < len(left) else None
      r = right[idx] if idx < len(right) else None
      check = check_order(l, r)
      if check != 0: return check
    return 0

total = 0

for idx, element in enumerate(data):
  [left, right] = element.split("\n")
  check = check_order(literal_eval(left), literal_eval(right))
  if check == 1: total += (idx + 1)

print(total)