print("03a.py")
print("------")

file = open("data/03.txt", "r")
data = file.read()

letters = map(lambda line: "".join(set(line[:len(line)//2]) & set(line[len(line)//2:])), data.split("\n"))
scores = map(lambda ltr: ord(ltr) - ord("a") + 1 if ltr.islower() else ord(ltr) - ord("A") + 27, letters)
score = sum(scores)

print(score)
