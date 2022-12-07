print("07b.py")
print("------")

file = open("data/07.txt", "r")
data = file.read()

commands = data.split("\n")

def parse_directory():
  command = commands.pop(0)

  children = []
  name = command[5::] # get name from "$ cd <name>"

  commands.pop(0) # skip "$ ls" and wait for data

  # parse files inside folders
  while len(commands) > 0 and commands[0][0] != "$":
    command = commands.pop(0)
    [size, file_name] = command.split(" ")
    if size != "dir":
      children.append({ "name": file_name, "size": int(size) })

  # parse child folders if there are any
  while len(commands) > 0:
    if ".." in commands[0]:
      commands.pop(0)
      return { "name": name, "children": children, "size": 0 }
    children.append(parse_directory())

  return { "name": name, "children": children, "size": 0 }

def calculate_size(directory):
  if directory["size"]: return

  summ = 0
  for child in directory["children"]:
    calculate_size(child)
    summ += child["size"]

  directory["size"] = summ

def find_directory_to_remove(directory):
  if "children" not in directory: return total

  smallest = total

  for child in directory["children"]:
    smallest = min(smallest, find_directory_to_remove(child))

  if directory["size"] > needed_space:
    smallest = min(smallest, directory["size"])

  return smallest

filesystem = parse_directory()
calculate_size(filesystem)

total = 70000000
free = 30000000

needed_space = free - (total - filesystem["size"])
to_remove = find_directory_to_remove(filesystem)

print(needed_space)
print(to_remove)
