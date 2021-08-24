'''
Running with Bunnies
====================

You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast! Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the solution is [1, 2].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 1, 1}, {1, 0, 1, 1, 1}, {1, 1, 0, 1, 1}, {1, 1, 1, 0, 1}, {1, 1, 1, 1, 0}}, 3)
Output:
    [0, 1]

Input:
Solution.solution({{0, 2, 2, 2, -1}, {9, 0, 2, 2, -1}, {9, 3, 0, 2, -1}, {9, 3, 2, 0, -1}, {9, 3, 2, 2, 0}}, 1)
Output:
    [1, 2]

-- Python cases --
Input:
solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
Output:
    [1, 2]

Input:
solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
Output:
    [0, 1]
'''

from copy import deepcopy
from itertools import permutations

def floyd(matrix):
    n = len(matrix)
    spaths = deepcopy(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if spaths[i][k] + spaths[k][j] < spaths[i][j]:
                    spaths[i][j] = spaths[i][k] + spaths[k][j]

    return spaths

def powerset(list):
    x = len(list)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, list) if i & mask]

def findMostBunnies(spaths, time_limit):
    n = len(spaths) - 2
    bunnyids = [num for num in range(n)]
    pset = powerset(bunnyids)
    pset = sorted(pset)
    optimal_bunnies = []
    for sub in pset:
        for permutation in permutations(sub):
            subsum = 0
            prev = 0
            next = len(spaths) - 1
            for bunnyid in permutation:
                next = bunnyid + 1
                subsum += spaths[prev][next]
                prev = next
            subsum += spaths[prev][len(spaths) - 1]
            if subsum <= time_limit and len(sub) > len(optimal_bunnies):
                optimal_bunnies = sub
                if len(optimal_bunnies) == n:
                    break
            else:
                pass
    return optimal_bunnies

def solution(times, time_limit):
    if len(times) <= 2:
        return []

    spaths = floyd(times)

    for i in range(len(spaths)):
        print(spaths[i])

    for i in range(len(spaths)):
        if (spaths[i][i] < 0):
            return [num for num in range(len(times) - 2)]

    return findMostBunnies(spaths, time_limit)


if __name__ == '__main__':
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print('', row)
    #print("Expected: [1, 2]\nCalculated:", str(solution(case2, 1)))
    print("Expected: [0, 1, 2]\nCalculated:", str(solution(case3, -500)))
