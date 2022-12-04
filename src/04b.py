print("04b.py")
print("------")

file = open("data/04.txt", "r")
data = file.read()

def check_overlap(pair):
  p1 = list(map(lambda v: int(v), pair[0].split("-")))
  p2 = list(map(lambda v: int(v), pair[1].split("-")))

  return (p1[0] <= p2[1] and p1[0] >= p2[0] or p1[1] <= p2[1] and p1[1] >= p2[0]) or (
    p2[0] <= p1[1] and p2[0] >= p1[0] or p2[1] <= p1[1] and p2[1] >= p1[0])

pairs = map(lambda line: line.split(","), data.split("\n"))
overlaps = map(lambda pair: check_overlap(pair), pairs)
result = sum(overlaps)

print(result)
