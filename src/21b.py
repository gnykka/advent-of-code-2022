print("21b.py")
print("------")

file = open("data/21.txt", "r")
data = file.read().split("\n")

def find_monkey_value(name):
  string = list(filter(lambda x: (" " + name) in x, data))[0]
  parsed = string.split(": ")

  monkey_1 = parsed[0]
  [monkey_2, sign, monkey_3] = parsed[1].split(" ")

  if monkey_1 == "root":
    return parse_monkey(monkey_3 if monkey_2 == name else monkey_2)

  monkey_1 = find_monkey_value(parsed[0])

  if sign == "+":
    if monkey_2 == name: return monkey_1 - parse_monkey(monkey_3)
    else: return monkey_1 - parse_monkey(monkey_2)

  if sign == "-":
    if monkey_2 == name: return monkey_1 + parse_monkey(monkey_3)
    else: return parse_monkey(monkey_2) - monkey_1

  if sign == "*":
    if monkey_2 == name: return monkey_1 / parse_monkey(monkey_3)
    else: return monkey_1 / parse_monkey(monkey_2)

  if sign == "/":
    if monkey_2 == name: return monkey_1 * parse_monkey(monkey_3)
    else: return parse_monkey(monkey_2) / monkey_1

def parse_monkey(name):
  string = list(filter(lambda x: x.startswith(name), data))[0]
  parsed = string.split(": ")

  operation = parsed[1].split(" ")

  # monkey yells a number — return that number
  if len(operation) == 1: return int(operation[0])

  [monkey_1, sign, monkey_2] = operation

  # monkey waits for the others — return the operation of the others
  if sign == "+": return parse_monkey(monkey_1) + parse_monkey(monkey_2)
  if sign == "-": return parse_monkey(monkey_1) - parse_monkey(monkey_2)
  if sign == "*": return parse_monkey(monkey_1) * parse_monkey(monkey_2)
  if sign == "/": return parse_monkey(monkey_1) / parse_monkey(monkey_2)

print(find_monkey_value("humn"))