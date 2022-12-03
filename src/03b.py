print("03b.py")
print("------")

file = open("data/03.txt", "r")
data = file.read()

packs = data.split("\n")
groups = [packs[i:i + 3] for i in range(0, len(packs), 3)]
letters = map(lambda group: "".join(set(group[0]) & set(group[1]) & set(group[2])), groups)
scores = map(lambda ltr: ord(ltr) - ord('a') + 1 if ltr.islower() else ord(ltr) - ord('A') + 27, letters)
score = sum(scores)

print(score)
