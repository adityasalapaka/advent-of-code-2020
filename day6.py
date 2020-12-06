filename = 'day6.txt'

# part 1

count = 0
yes = set()
for line in open(filename,'r'):

	if line == '\n':
		count += len(yes)
		yes = set()
		continue

	[yes.add(answer) for answer in line.split()[0]]

count += len(yes)
print(count)

# part 2

count = 0
sets = []
for line in open(filename,'r'):
	yes = set()
	
	if line == '\n':
		count += len(set.intersection(*sets))
		sets = []
		continue

	[yes.add(answer) for answer in line.split()[0]]
	sets.append(yes)

count += len(set.intersection(*sets))
print(count)