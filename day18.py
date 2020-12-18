filename = 'day18.txt'

def evaluate(eq:str):
	eq = eq.split(' ')

	x = ' '.join(eq[:3])

	while len(eq) > 1:
		x = ' '.join(eq[:3])
		eq = [str(eval(x))] + eq[3:]

	return eq[0]

def parenthetic_contents(string:str):
	"""Generate parenthesized contents in string as pairs (level, contents)."""
	stack = []
	for i, c in enumerate(string):
		if c == '(':
			stack.append(i)
		elif c == ')' and stack:
			start = stack.pop()
			yield (string[start + 1: i])
			break

# part 1
s = 0
for line in open(filename,'r'):
	eq = line.strip()

	# solve brackets first
	while list(parenthetic_contents(eq)):
		brackets = list(parenthetic_contents(eq))
		eq = eq.replace('('+brackets[0]+')', evaluate(brackets[0]))

	s += int(evaluate(eq))

print(s)

# part 2
def evaluate_part2(eq:str):
	eq = eq.split(' ')

	# in case of + wrap brackets around operands
	for i, c in enumerate(eq):
		if c == '+':
			eq[i-1] = '(' + eq[i-1]
			eq[i+1] = eq[i+1] + ')'

	eq = ' '.join(eq)

	while list(parenthetic_contents(eq)):
		brackets = list(parenthetic_contents(eq))
		eq = eq.replace('('+brackets[0]+')', evaluate(brackets[0]))

	return evaluate(eq)

s = 0
for line in open(filename,'r'):
	eq = line.strip()

	while list(parenthetic_contents(eq)):
		brackets = list(parenthetic_contents(eq))
		eq = eq.replace('('+brackets[0]+')', evaluate_part2(brackets[0]))

	s += int(evaluate_part2(eq))

print(s)