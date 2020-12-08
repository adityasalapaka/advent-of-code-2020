# Advent of Code 2020
Solutions for Advent of Code 2020 in Python 3, supplemented by some additional reading and my notes.

| Problem | Solution | Additional Reading | Notes |
|   :--:  |   :--:   |         :--:       |  :-- |
|[**Day 1: Report Repair**](https://adventofcode.com/2020/day/1)|[day1.py](day1.py)| [Two Sum Problem](https://coderbyte.com/algorithm/two-sum-problem) | The input size is small enough to brute-force it using the naive approach.  
|[**Day 2: Password Philosophy**](https://adventofcode.com/2020/day/2)|[day2.py](day2.py)| [collections.Counter](https://docs.python.org/3.9/library/collections.html#collections.Counter)|-|
|[**Day 3: Toboggan Trajectory**](https://adventofcode.com/2020/day/3)|[day3.py](day3.py)|-|It's not immediately obvious but the map repeats when you reach the rightmost edge. The tour terminates at the bottom of the map only. This is why the `duplicate` operation is implemented.|
|[**Day 4: Passport Processing**](https://adventofcode.com/2020/day/4)|[day4.py](day4.py)|[all()](https://docs.python.org/3.9/library/functions.html#all)<br>[On Python's multiple conditionals](https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/)|-|
|[**Day 5: Binary Boarding**](https://adventofcode.com/2020/day/5)|[day5.py](day5.py)|-|-|
|[**Day 6: Custom Customs**](https://adventofcode.com/2020/day/6)|[day6.py](day6.py)|[set.intersection()](https://docs.python.org/3.9/library/stdtypes.html#frozenset.intersection)<br> [List Unpacking in Python](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/)|-|
|[**Day 7: Handy Haversacks**](https://adventofcode.com/2020/day/7)|[day7.py](day7.py)|[NetworkX](https://networkx.org/documentation/stable/index.html), a graph library for Python|Figuring out that it was easier to include the source node itself while recursing took embarrassingly long. The test cases provided really helped debug the solution.
|[**Day 8: Handheld Halting**](https://adventofcode.com/2020/day/8)|[day8.py](day8.py)|[copy — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)|In Part 2, `file_new = file` would simply create a reference to `file` in `file_new`, so changing one object changes the other. Therefore, a shallow or deep copy of the `list` objected is needed, which is done using the `copy()` method.