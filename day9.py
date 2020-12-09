from itertools import combinations

filename = 'day9.txt'

# part 1
preamble = 25
file = []

i = 0

for line in open(filename,'r'):
	if i < preamble:
		file.append(int(line))
		i += 1
		continue

	if int(line) not in [a[0]+a[1] for a in combinations(file[-preamble:],2)]:
		invalid = int(line)
		break

	file.append(int(line))
	
print(invalid)

# part 2
file = [int(elem) for elem in open(filename,'r').readlines()]

flag = False

for lower in range(len(file)):
	for upper in range(lower,len(file)):

		if sum(file[lower:upper]) == invalid:
			flag = True
			break

		elif sum(file[lower:upper]) > invalid:
			break

	if flag:
		break

	if sum(file[lower:upper]) > invalid:
		continue

print(min(file[lower:upper]) + max(file[lower:upper]))