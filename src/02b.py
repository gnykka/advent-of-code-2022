print("02a.py")
print("------")

file = open("data/02.txt", "r")
data = file.read()

rules = {
  "AX": "C", "AY": "A", "AZ": "B",
  "BX": "A", "BY": "B", "BZ": "C",
  "CX": "B", "CY": "C", "CZ": "A",
}

rounds = map(lambda line: line.split(" "), data.split("\n"))
scores = map(lambda rnd: ord(rules[rnd[0] + rnd[1]]) - ord("A") + 1 + (ord(rnd[1]) - ord("X")) * 3, rounds)
score = sum(scores)

print(score)