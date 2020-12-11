filename = 'day11.txt'

import numpy as np 

file = [elem.strip() for elem in open(filename,'r').readlines()]

# part 1
def adjacent(row:int, col:int, seats:np.ndarray) -> list:
	rows, cols = np.shape(seats)

	row1 = max(0, row-1)
	row2 = min(row+1, rows-1)

	col1 = max(0, col-1)
	col2 = min(col+1, cols-1)

	adj = list(seats[row1:row2+1, col1:col2+1].flatten())
	adj.remove(seats[row,col]) # remove current seat itself

	return adj

seats = np.array([[elem for elem in line] for line in file])

new_seats = np.zeros(np.shape(seats),'str')

flag = False
while not np.array_equal(seats, new_seats):

	if flag:
		seats = np.copy(new_seats)
		
	else:	
		flag = True

	for row in range(len(seats)):

		for col in range(len(seats[row])):

			adj = adjacent(row,col,seats)

			if seats[row,col] == 'L' and all([elem != '#' for elem in adj]):
				new_seats[row,col] = '#'

			elif seats[row,col] == '#' and sum([elem == '#' for elem in adj]) >= 4:
				new_seats[row,col] = 'L'

print(sum(new_seats.flatten()=='#'))

# part 2
def line_of_sight(row:int, col:int, seats:np.ndarray) -> list:
	rows, cols = np.shape(seats)

	adj = np.zeros((3,3),'str')
	adj[1,1] = seats[row,col]

	directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

	for direction in directions:
		vertical, horizontal = direction

		while 0 <= row+vertical <= rows-1 and 0 <= col+horizontal <= cols-1 and seats[row+vertical, col+horizontal] == '.':

			vertical += direction[0]
			horizontal += direction[1]

		if 0 <= row+vertical <= rows-1 and 0 <= col+horizontal <= cols-1:

			adj[1+direction[0],1+direction[1]] = seats[row+vertical, col+horizontal]

	adj = list(adj.flatten())
	adj.remove(seats[row,col])
	return adj 

seats = np.array([[elem for elem in line] for line in file])

new_seats = np.full(np.shape(seats), fill_value='.', dtype=str)

flag = False
while not np.array_equal(seats, new_seats):

	if flag:
		seats = np.copy(new_seats)
		
	else:	
		flag = True

	for row in range(len(seats)):

		for col in range(len(seats[row])):

			adj = line_of_sight(row,col,seats)
			
			if seats[row,col] == 'L' and all([elem != '#' for elem in adj]):
				new_seats[row,col] = '#'

			elif seats[row,col] == '#' and sum([elem == '#' for elem in adj]) >= 5:
				new_seats[row,col] = 'L'

print(sum(new_seats.flatten()=='#'))