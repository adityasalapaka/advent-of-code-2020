filename = 'day14.txt'

from collections import defaultdict
from itertools import product

# part 1
mem = defaultdict(int)

for line in open(filename,'r'):
	line = line.strip().split('=')
	
	if line[0][:4] == 'mask':
		mask = line[1].strip()

	else:
		index = int(''.join(filter(str.isdigit, line[0])))

		value = int(line[1])
		value = bin(value)[2:].zfill(len(mask)) # pad with zeros

		result = ''.join([value[i] if mask[i] == 'X' else mask[i] for i in range(len(mask))])
		result = int(result,2) # convert to base 10
		
		mem[index] = result

print(sum(mem.values()))

# part 2
mem = defaultdict(int)

for line in open(filename,'r'):
	line = line.strip().split('=')
	
	if line[0][:4] == 'mask':
		mask = line[1].strip()

	else:
		index = int(''.join(filter(str.isdigit, line[0])))
		value = int(line[1])

		index = bin(index)[2:].zfill(len(mask)) # pad with zeros

		result = [index[i] if mask[i] == '0' else mask[i] for i in range(len(mask))]
		
		C = result.count('X')
		floating = list(product(range(2),repeat=C)) # makes ((0,1) (1,0) (1,1) (0,0))

		indexes = [i for i, bit in enumerate(result) if bit == 'X']
		
		for pairs in floating:
			index_floating = result
			for i in range(C):
				index_floating[indexes[i]] = str(pairs[i])
			index_floating = int(''.join(index_floating),2)
			mem[index_floating] = value

print(sum(mem.values()))