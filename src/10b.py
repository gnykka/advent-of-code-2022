print("10b.py")
print("------")

file = open("data/10.txt", "r")
data = file.read()

commands = data.split("\n")

index = 0
value = 1

length = 240
line_length = 40
result = list("." * length)

for command in commands:
  command_parts = command.split(" ")
  word = command_parts[0]
  count = 0 if len(command_parts) == 1 else int(command_parts[1])

  # start of cycle — inc index and render pixel
  index += 1
  line_index = index % line_length
  if value >= line_index - 2 and value <= line_index:
    result[index - 1] = "#"

  if word == "addx":
    # next cycle — inc index and render pixel
    index += 1
    line_index = index % line_length
    if value >= line_index - 2 and value <= line_index:
      result[index - 1] = "#"

    value += count

result_str = "".join(result)
lines = [result_str[i:i+line_length] for i in range(0, len(result), line_length)]

for line in lines:
  print(line)
