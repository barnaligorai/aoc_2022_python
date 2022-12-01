# # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def read_file(file):
  input_file = open(file)
  input = input_file.read()
  input_file.close()
  return input  

def to_list(raw_list,seperator):
  return raw_list.split(seperator)

def parse_one_elf_calories(raw_calories):
  one_elf_raw_calories = to_list(raw_calories,"\n")
  return map(int,one_elf_raw_calories)

def parse_calories(raw_input):
  raw_calories = to_list(raw_input,'\n\n')
  return map(lambda one_elf_calories:parse_one_elf_calories(one_elf_calories),raw_calories)


raw_calories = read_file("./input.txt")
each_elfs_calories = parse_calories(raw_calories)
each_elfs_total_calories = map(sum,each_elfs_calories)

maxCalories = max(each_elfs_total_calories)
print(maxCalories)

# ----------- part 2 -------------

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

calories = each_elfs_total_calories[:]
calories.sort()
calories_of_max_3 = sum(calories[-3:])
print(calories_of_max_3)
