from collections import defaultdict

filename = 'day10.txt'

# part 1
adapters = [int(elem) for elem in open(filename,'r').readlines()]

voltage = 0
diffs = [0,0,0]

while adapters:
	for i in range(1,4):

		if voltage + i in adapters:
			adapters.remove(voltage + i)
			voltage += i

			diffs[i-1] += 1

			break

voltage += 3
diffs[2] += 1

print(diffs[0]*diffs[2])

# part 2
adapters = [int(elem) for elem in open(filename,'r').readlines()]
adapters.append(0)
adapters.append(voltage)
adapters.sort()

paths = defaultdict(int) # takes care of unavailable indexes
paths[0] = 1 # only 1 path to origin, origin itself

for i in adapters[1:]:
	paths[i] = paths[i-1] + paths[i-2] + paths[i-3] # how many paths to i from i-1 through i-3?

print(paths[voltage])