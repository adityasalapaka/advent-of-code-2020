import numpy as np
from scipy.ndimage import convolve

filename = 'day17.txt'

grid = [line.strip() for line in open(filename,'r')]
grid = np.zeros((len(grid), len(grid)), dtype=int)

for i, line in enumerate(open(filename,'r')):
	line = line.strip()

	for j, c in enumerate(line):
		grid[i,j] = 0 if c == '.' else 1 

def solver(grid:np.ndarray, dim:int):
	# add extra dimension to grid to make it N-D
	grid = np.expand_dims(grid, axis=tuple(range(dim-2)))

	# convolve filter to count neighbours
	conv = np.ones(shape=(3,) * dim)

	# to ignore the current cube itself
	conv[(1,) * dim] = 0

	# change from # of neighbours to active/inactive based on rules

	for _ in range(6):

		# pad in all directions across
		grid = np.pad(grid, pad_width=1, mode='constant', constant_values=0).astype(int) # to convert bool to int

		neighbours = convolve(grid, conv, mode='constant', cval=0)

		grid = ((grid==1) & ((neighbours==2) | (neighbours==3))) | ((grid==0) & (neighbours==3))

	return np.sum(grid)

# part 1
print(solver(grid, 3))

# part 2
print(solver(grid, 4))