print("04a.py")
print("------")

file = open("data/04.txt", "r")
data = file.read()

def check_include(pair):
  p1 = list(map(lambda v: int(v), pair[0].split("-")))
  p2 = list(map(lambda v: int(v), pair[1].split("-")))

  return p1[0] <= p2[0] and p1[1] >= p2[1] or p2[0] <= p1[0] and p2[1] >= p1[1]

pairs = map(lambda line: line.split(","), data.split("\n"))
includes = map(lambda pair: check_include(pair), pairs)
result = sum(includes)

print(result)
