import math

print("11b.py")
print("------")

file = open("data/11.txt", "r")
data = file.read()

monkeys_data = data.split("\n\n")

state = []
for m_data in monkeys_data:
  lines = m_data.split("\n")

  items = list(map(lambda l: int(l), lines[1][18:].split(", ")))
  operation = lines[2][19:].split(" ")
  division = int(lines[3].split("by ")[1])

  check_0 = int(lines[5][30:])
  check_1 = int(lines[4][29:])

  state.append({
    "items": items,
    "operation": {
      "name": operation[1],
      "value": operation[2] if operation[2] == "old" else int(operation[2])
    },
    "division": division,
    "check": [check_0, check_1],
    "inspections": 0,
  })

divisions = 1
for s in state:
  divisions = divisions * s["division"]

index = 1

while index <= 10000:
  for monkey in state:
    while len(monkey["items"]) > 0:
      item = monkey["items"].pop()

      # monkey inspects item
      monkey["inspections"] += 1

      value = monkey["operation"]["value"]
      value = item if value == "old" else value

      item = item * value if monkey["operation"]["name"] == "*" else item + value

      # check division
      check = item % monkey["division"] == 0
      next_monkey = monkey["check"][1] if check else monkey["check"][0]

      item = item % divisions

      # throw to next monkey
      state[next_monkey]["items"].append(item)

  index += 1

inspections = list(map(lambda m: m["inspections"], state))
inspections.sort(reverse=True)

print(inspections[0] * inspections[1])

