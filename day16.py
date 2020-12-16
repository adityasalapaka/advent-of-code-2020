filename = 'day16.txt'

from collections import defaultdict

# part 1
valid_ranges = set()

file = open(filename,'r').readlines()

i = 0

for line in file:
	if line == '\n':
		i += 2
		break
	field, ranges = line.split(':')
	for R in ranges.strip().split('or'):
		R = R.strip()
		lower,upper = R.split('-')
		[valid_ranges.add(x) for x in list(range(int(lower),int(upper)+1))]

	i+= 1

ticket = [int(x) for x in file[i].split(',')]

i += 3

invalid = 0
discard_pile = []
for line in file[i:]:

	for x in line.split(','):

		if int(x) not in valid_ranges:
			invalid += int(x)
			discard_pile.append(i)

	i += 1

print(invalid)

# part 2
valid_ranges = defaultdict(set)

file = open(filename,'r').readlines()

# discard invalid tickets
for discard in sorted(discard_pile, reverse = True):
	del file[discard]

i = 0

# get valid ranges by field
for line in file:
	if line == '\n':
		i += 2
		break
	field, ranges = line.split(':')
	for R in ranges.strip().split('or'):
		R = R.strip()
		lower,upper = R.split('-')
		[valid_ranges[field].add(x) for x in list(range(int(lower),int(upper)+1))]

	i+= 1

ticket = [int(x) for x in file[i].split(',')]

i += 3

nearby_tickets = [set() for _ in range(len(ticket))]

# get values by position
for line in file[i:]:
	
	[nearby_tickets[pos].add(int(value)) for pos, value in enumerate(line.split(','))]

# identify all valid sets 
ticket_fields = defaultdict(set)

for i, pos in enumerate(nearby_tickets):
	
	[ticket_fields[key].add(i) for key, value in valid_ranges.items() if pos == pos & value]

# sort sets by length of each valid set and get only fields by elimination
removed = set()
for k,v in sorted(ticket_fields.items(), key=lambda k: len(k[1])):
	value = (v-removed).pop()
	removed.add(value)

	ticket_fields[k] = value

departure = 1
for key, value in ticket_fields.items():
	if 'departure' in key:
		departure *= ticket[value]

print(departure)