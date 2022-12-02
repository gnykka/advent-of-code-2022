print("02a.py")
print("------")

file = open("data/02.txt", "r")
data = file.read()

# rock (A) > scissors (C)
# rock (A) < paper (B)
# paper (B) < scissors (C)

rules = {
  "XA": 0, "XB": -1, "XC": 1,
  "YA": 1, "YB": 0, "YC": -1,
  "ZA": -1, "ZB": 1, "ZC": 0,
}

rounds = map(lambda line: line.split(" "), data.split("\n"))
scores = map(lambda rnd: ord(rnd[1]) - ord("X") + 1 + rules[rnd[1] + rnd[0]] * 3 + 3, rounds)
score = sum(scores)

print(score)