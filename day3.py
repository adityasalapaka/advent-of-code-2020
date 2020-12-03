# part 1

filename = 'day3.txt'

with open(filename,'r') as f:
	f.readline()

	trees = 0
	right = 3
	duplication = 1

	for line in f:
		line = line.split()[0]

		if right>=len(line):
			duplication = duplication + 1
		line = line*duplication

		if line[right] == '#':
			trees += 1
			
		right += 3

print(trees)

# part 2

def slope(right_increment:int = 1, down_increment:int = 1) -> int:
	filename = 'day3.txt'

	trees = 0
	duplication = 1
	right = right_increment
	down = down_increment

	with open(filename,'r') as f:

		for _ in range(down_increment):
			line = f.readline()

		for line in f:
			if down % down_increment !=0 :
				down += 1
				continue

			line = line.split()[0]

			if right>=len(line):
				duplication = duplication + 1
			line = line*duplication

			if line[right] == '#':
				trees += 1

			right += right_increment
			down += 1

	return trees

print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))