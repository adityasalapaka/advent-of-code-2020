filename = 'day1.txt'

report = {}
for line in open(filename,'r'):
	report[int(line)] = 1

# part 1
for line,_ in report.items():
	if (2020-line) in report:
		break

print(line*(2020-line))

# part 2
flag = 0
for line,_ in report.items():
	for line2,_ in report.items():
		if (2020-line-line2) in report:
			print(line, line2, 2020-line-line2)
			flag=1
			break
	if flag == 1:
		break

print(line*line2*(2020-line-line2))