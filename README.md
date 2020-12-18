# Advent of Code 2020
Solutions for Advent of Code 2020 in Python 3, supplemented by some additional reading and my notes.

| Problem | Solution | Additional Reading | Notes |
|   :--:  |   :--:   |         :--:       |  :-- |
|[**Day 1: Report Repair**](https://adventofcode.com/2020/day/1)|[day1.py](day1.py)| [Two Sum Problem](https://coderbyte.com/algorithm/two-sum-problem) | The input size is small enough to brute-force it using the naive approach.  
|[**Day 2: Password Philosophy**](https://adventofcode.com/2020/day/2)|[day2.py](day2.py)| [`collections.Counter`](https://docs.python.org/3.9/library/collections.html#collections.Counter)|-|
|[**Day 3: Toboggan Trajectory**](https://adventofcode.com/2020/day/3)|[day3.py](day3.py)|-|It's not immediately obvious but the map repeats when you reach the rightmost edge. The tour terminates at the bottom of the map only. This is why the `duplicate` operation is implemented.|
|[**Day 4: Passport Processing**](https://adventofcode.com/2020/day/4)|[day4.py](day4.py)|[`all()`](https://docs.python.org/3.9/library/functions.html#all)<br>[On Python's multiple conditionals](https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/)|-|
|[**Day 5: Binary Boarding**](https://adventofcode.com/2020/day/5)|[day5.py](day5.py)|-|-|
|[**Day 6: Custom Customs**](https://adventofcode.com/2020/day/6)|[day6.py](day6.py)|[`set.intersection()`](https://docs.python.org/3.9/library/stdtypes.html#frozenset.intersection)<br> [List Unpacking in Python](https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/)|-|
|[**Day 7: Handy Haversacks**](https://adventofcode.com/2020/day/7)|[day7.py](day7.py)|[NetworkX](https://networkx.org/documentation/stable/index.html), a graph library for Python|Figuring out that it was easier to include the source node itself while recursing took embarrassingly long. The test cases provided really helped debug the solution.
|[**Day 8: Handheld Halting**](https://adventofcode.com/2020/day/8)|[day8.py](day8.py)|[`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)|In Part 2, `file_new = file` would simply create a reference to `file` in `file_new`, so changing one object changes the other. Therefore, a shallow or deep copy of the `list` objected is needed, which is done using the `copy()` method.
|[**Day 9: Encoding Error**](https://adventofcode.com/2020/day/9)|[day9.py](day9.py)|[`itertools.combinations`](https://docs.python.org/3.9/library/itertools.html#itertools.combinations)|-|
|[**Day 10: Adapter Array**](https://adventofcode.com/2020/day/10)|[day10.py](day10.py)|[`collections.defaultdict`](https://docs.python.org/3.9/library/collections.html#collections.defaultdict)|While a brute-force solution worked for the smaller inputs, a [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) approach was eventually needed to solve the larger input size
[**Day 11: Seating System**](https://adventofcode.com/2020/day/11)|[day11.py](day11.py)|-|Quickly gave up the idea of dealing with this using 2D lists. `numpy`, `np.flatten()` in particular, was extremely helpful
[**Day 12: Rain Risk**](https://adventofcode.com/2020/day/12)|[day12.py](day12.py)|[Rotation of axes](https://en.wikipedia.org/wiki/Rotation_of_axes)|Rotating `relative_waypoint` is easier than rotating `waypoint` given that it's effectively rotation around the origin, which is the ship itself.|
[**Day 13: Shuttle Search**](https://adventofcode.com/2020/day/13)|[day13.py](day13.py)|[Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)|This wasn't much of a programming puzzle, but rather depended upon knowing about the existence of the Chinese remainder theorem A good explanation can be found [here](https://www.youtube.com/watch?v=zIFehsBHB8o).|
[**Day 14: Docking Data**](https://adventofcode.com/2020/day/14)|[day14.py](day14.py)|[`itertools.product`](https://docs.python.org/3.9/library/itertools.html#itertools.product)|-|
[**Day 15: Rambunctious Recitation**](https://adventofcode.com/2020/day/15)|[day15.py](day15.py)|[`tqdm`](https://github.com/tqdm/tqdm)|This is still a brute-force solution but would like to find a more constructive solution, ideally. <br>(Optional) Used `tqdm` to see the progress of solution computation. 
[**Day 16: Ticket Translation**](https://adventofcode.com/2020/day/16)|[day16.py](day16.py)|-|-|
[**Day 17: Conway Cubes**](https://adventofcode.com/2020/day/17)|[day17.py](day17.py)|[`scipy.ndimage.convolve`](https://docs.scipy.org/doc/scipy-1.5.4/reference/generated/scipy.ndimage.convolve.html#scipy.ndimage.convolve)|Understanding the example itself took quite some time. This is one of those problems which becomes progressively unsolvable the more you think about it. Writing a general purpose solution with `numpy` that worked for all symmetrical dimensions was very helpful.