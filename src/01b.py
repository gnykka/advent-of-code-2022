print("01b.py")
print("------")

file = open("data/01.txt", "r")
data = file.read()

elves = data.split("\n\n")
calories = map(lambda elf: sum(map(int, elf.split("\n"))), elves)
maximum = sum(sorted(calories, reverse = True)[0:3])

print(maximum)