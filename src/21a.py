print("21a.py")
print("------")

file = open("data/21.txt", "r")
data = file.read().split("\n")

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

print(parse_monkey("root"))