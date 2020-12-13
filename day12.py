filename = 'day12.txt'

# part 1
pos = [0,0] #[x,y]
orientations = [[1,0], [0,1], [-1,0], [0,-1]]
i = 0
orientation = orientations[i]

for line in open(filename,'r'):
	line = line.strip()

	direction = line[0]
	value = int(line[1:])

	if direction == 'N':
		pos[1] += value

	elif direction == 'S':
		pos[1] -= value

	elif direction == 'E':
		pos[0] += value

	elif direction == 'W':
		pos[0] -= value

	elif direction == 'F':
		pos[0] += list(value*x for x in orientation)[0]
		pos[1] += list(value*x for x in orientation)[1]

	elif direction == 'L':
		for _ in range(value//90):
			i += 1
			if i > 3:
				i = 0

		orientation = orientations[i]

	elif direction == 'R':
		for _ in range(value//90):
			i -= 1
			if i < 0:
				i = 3

		orientation = orientations[i]

print(sum(list(map(abs, pos))))

# part 2
pos = [0,0] #[x,y]
waypoint = [10,1]
waypoint_relative = [10,1]

for line in open(filename,'r'):
	line = line.strip()

	direction = line[0]
	value = int(line[1:])

	if direction == 'N':
		waypoint[1] += value
		waypoint_relative[1] += value

	elif direction == 'S':
		waypoint[1] -= value
		waypoint_relative[1] -= value

	elif direction == 'E':
		waypoint[0] += value
		waypoint_relative[0] += value

	elif direction == 'W':
		waypoint[0] -= value
		waypoint_relative[0] -= value

	elif direction == 'F':
		pos[0] += value*(waypoint_relative[0])
		pos[1] += value*(waypoint_relative[1])

		waypoint[0], waypoint[1] = pos[0] + waypoint_relative[0], pos[1] + waypoint_relative[1]

	elif direction == 'L':
		for _ in range(value//90):
			waypoint_relative[0], waypoint_relative[1] = -waypoint_relative[1], waypoint_relative[0]

		waypoint[0], waypoint[1] = pos[0] + waypoint_relative[0], pos[1] + waypoint_relative[1]

	elif direction == 'R':
		for _ in range(value//90):
			waypoint_relative[0], waypoint_relative[1] = waypoint_relative[1], -waypoint_relative[0]

		waypoint[0], waypoint[1] = pos[0] + waypoint_relative[0], pos[1] + waypoint_relative[1]

print(sum(list(map(abs, pos))))