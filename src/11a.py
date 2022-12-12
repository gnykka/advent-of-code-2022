import math

print("11a.py")
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

index = 1

while index <= 20:
  for monkey in state:
    while len(monkey["items"]) > 0:
      item = monkey["items"].pop()

      # monkey inspects item
      monkey["inspections"] += 1

      value = item if monkey["operation"]["value"] == "old" else monkey["operation"]["value"]
      item = item * value if monkey["operation"]["name"] == "*" else item + value

      # gets bored
      item = math.floor(item / 3)

      # check division
      next_monkey = monkey["check"][int(item % monkey["division"] == 0)]

      # throw to next monkey
      state[next_monkey]["items"].append(item)

  index += 1

inspections = list(map(lambda m: m["inspections"], state))
inspections.sort(reverse=True)

print(inspections[0] * inspections[1])

