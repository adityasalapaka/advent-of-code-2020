# part 1
filename = 'day4.txt'

valid = 0
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
passport = []
for line in open(filename,'r'):

	if line == '\n':
		if all(elem in passport for elem in fields):
			valid += 1
		passport = []
		continue

	for elm in line.split(' '):
		passport.append(elm.split(':')[0])

if all(elem in passport for elem in fields):
	valid += 1

print(valid)

# part 2
import re
filename = 'day4.txt'

valid = 0
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
passport = {}

def rules(passport:dict):

	def hgt_validation(value:str):

		if value[-2:] == 'cm':
			return 150 <= int(value[:-2]) <= 193
		else:
			return 59 <= int(value[:-2]) <= 76

	rules = [1920 <= int(passport['byr']) <= 2002,
			 2010 <= int(passport['iyr']) <= 2020,
			 2020 <= int(passport['eyr']) <= 2030,
			 hgt_validation(passport['hgt']),
			 all([passport['hcl'][0] == '#', len(passport['hcl'][1:]) == 6, re.match(r"^[A-Fa-f0-9]+$",passport['hcl'][1:])]),
			 passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'],
			 len(passport['pid']) == 9]

	return rules

for line in open(filename,'r'):

	if line == '\n':

		if all(elem in passport for elem in fields) and all(rules(passport)):
			valid +=1

		passport = {}
		continue

	for elm in line.split(' '):
		key, value = elm.split(':')

		passport[key] = value.strip()

if all(elem in passport for elem in fields) and all(rules(passport)):
	valid +=1

print(valid)