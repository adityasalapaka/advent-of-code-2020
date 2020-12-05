filename = 'day5.txt'

seatids = []

for line in open(filename,'r'):

	line = line.split()[0]

	front = 0
	back = 127

	for c in line[:7]:
		if c == 'F':
			back = int((front+back)/2)
		if c == 'B':
			front = int((front+back)/2) + 1

	left = 0
	right = 7

	for c in line[7:]:
		if c == 'L':
			right = int((left+right)/2)
		if c == 'R':
			left = int((left+right)/2) + 1

	seatid = (front*8) + left

	seatids.append(seatid)

# part 1
print(max(seatids))

# part 2
for seat in seatids:
	if seat + 1 not in seatids:
		print(seat + 1)
		break