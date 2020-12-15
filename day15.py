file = [9,12,1,4,17,0,18]

from collections import defaultdict
from tqdm import tqdm

def compute_last_spoken(memory:list, nth_number_spoken:int) -> int:
	memory = file.copy()
	spoken = defaultdict(list)

	for i in range(len(memory)):
		
		spoken[memory[i]].append(i)
		last = memory[i]

	i +=1 

	for i in tqdm(range(i, nth_number_spoken), initial = i, total = nth_number_spoken):

		last_spoken_times = len(spoken[last])

		if last_spoken_times == 1:
			spoken[0].append(i)
			last = 0
		else:
			indices = spoken[last]
			last = indices[-1] - indices[-2]
			spoken[last].append(i)

	return last

# part 1
print(compute_last_spoken(file, 2020))

# part 2
print(compute_last_spoken(file, 30000000))