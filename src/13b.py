from ast import literal_eval

print("13b.py")
print("------")

file = open("data/13.txt", "r")
data = list(filter(None, file.read().split("\n")))

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

index_2 = 0
index_6 = 0

for line in data:
  parsed = literal_eval(line)

  check_2 = check_order(parsed, [[2]])
  check_6 = check_order(parsed, [[6]])

  if check_2 == 1: index_2 += 1
  if check_6 == 1: index_6 += 1

print((index_2 + 1) * (index_6 + 2))