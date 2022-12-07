import re

print("05.py")
print("------")

file = open("data/05.txt", "r")
data = file.read()

[data_state, data_instructions] = data.split("\n\n")

# parse the state
data_state = data_state.split("\n")[::-1]
stacks_count = len(re.findall(r"[0-9]+", data_state[0]))
state = []

for i in range(stacks_count):
  state.append([])
  for line in data_state[1::]:
    crate = line[i * 4 + 1]
    if crate != " ": state[i].append(crate)

# move the crates according to instructions
for instruction in data_instructions.split("\n"):
  values = list(map(lambda v: int(v), re.findall(r"[0-9]+", instruction)))

  count = values[0]
  from_crate = values[1] - 1
  to_crate = values[2] - 1

  crates = state[from_crate][-count:][::-1] # remove "[::-1]" for part b

  state[to_crate] += crates
  del state[from_crate][len(state[from_crate]) - count:]

crates = "".join(map(lambda s: s[len(s) - 1], state))

print(crates)

