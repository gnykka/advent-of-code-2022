print("10a.py")
print("------")

file = open("data/10.txt", "r")
data = file.read()

commands = data.split("\n")

def calc_strenght(index, value, cycle):
  for command in commands:
    command_parts = command.split(" ")
    word = command_parts[0]
    count = 0 if len(command_parts) == 1 else int(command_parts[1])

    if (
      word == "noop" and index == cycle or
      word == "addx" and (index == cycle or index == cycle - 1)
    ): return cycle * value

    if word == "noop": index += 1
    if word == "addx":
      index += 2
      value += count

  return index * value

cycles = [20, 60, 100, 140, 180, 220]
index = 1
value = 1
total = 0

for cycle in cycles:
  total += calc_strenght(index, value, cycle)

print(total)
