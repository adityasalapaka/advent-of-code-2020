filename = 'day8.txt'

with open(filename,'r') as f:
	file = f.readlines()

# part 1
accumulator = 0
pointer = 0
pointers = []

while True:

	if pointer in pointers:
		break

	operation, instruction = file[pointer].split(' ')

	pointers.append(pointer)
	
	if operation == 'nop':
		pass

	elif operation == 'acc':
		accumulator += int(instruction)

	elif operation == 'jmp':
		pointer += int(instruction)
		continue

	pointer += 1

print(accumulator)

# part 2
def execute(file:list) -> int:
	accumulator = 0
	pointer = 0
	pointers = []

	while pointer < len(file):
		if pointer in pointers:
			return None

		operation, instruction = file[pointer].split(' ')

		pointers.append(pointer)
		
		if operation == 'nop':
			pass

		elif operation == 'acc':
			accumulator += int(instruction)

		elif operation == 'jmp':
			pointer += int(instruction)
			continue

		pointer += 1

	return accumulator

for i in range(len(file)):

	if file[i].split(' ')[0] == 'jmp':
		file_new = file.copy()
		file_new[i] = file_new[i].replace('jmp', 'nop')

	elif file[i].split(' ')[0] == 'nop':
		file_new = file.copy()
		file_new[i] = file_new[i].replace('nop', 'jmp')

	else:
		continue

	accumulator = execute(file_new)

	if accumulator is not None:
		break

print(accumulator)