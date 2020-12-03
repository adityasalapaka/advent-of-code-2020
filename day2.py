from collections import Counter

filename = 'day2.txt'

# part 1
valid = 0
for line in open(filename,'r'):
	line = line.split(' ')
	lower, upper = line[0].split('-')
	character = line[1][0]
	password = line[2].split()[0]
	if int(lower) <= Counter(password)[character] <= int(upper):
		valid += 1

print(valid)

# part 2
valid = 0
for line in open(filename,'r'):
	line = line.split(' ')
	lower, upper = line[0].split('-')
	character = line[1][0]
	password = line[2].split()[0]
	if (password[int(lower)-1] == character and password[int(upper)-1] != character) or (password[int(lower)-1] != character and password[int(upper)-1] == character):
		valid += 1

print(valid)