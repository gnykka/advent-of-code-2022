print("06.py")
print("------")

file = open("data/06.txt", "r")
data = file.read()

step = 4 # 14 for part b
count = len(data)

while len(data) > step:
  substring = data[0:step]
  if len(set(substring)) == len(substring):
    break
  data = data[1:]

index = count - len(data) + step

print(index)