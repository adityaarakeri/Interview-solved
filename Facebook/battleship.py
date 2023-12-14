"""
You're playing Battleship on a grid of cells with 
�
R rows and 
�
C columns. There are 
0
0 or more battleships on the grid, each occupying a single distinct cell. The cell in the 
�
ith row from the top and 
�
jth column from the left either contains a battleship (
�
�
,
�
=
1
G 
i,j
​
 =1) or doesn't (
�
�
,
�
=
0
G 
i,j
​
 =0).
You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the 
�
∗
�
R∗C possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.
Your task is to implement the function getHitProbability(R, C, G) which returns this probability.
Note: Your return value must have an absolute or relative error of at most 
1
0
−
6
10 
−6
  to be considered correct.
Constraints
1
≤
�
,
�
≤
1
0
0
1≤R,C≤100
0
≤
�
�
,
�
≤
1
0≤G 
i,j
​
 ≤1
Sample test case #1
R = 2
C = 3
G = 0 0 1
    1 0 1
Expected Return Value = 0.50000000
Sample test case #2
R = 2
C = 2
G = 1 1
    1 1
Expected Return Value = 1.00000000
Sample Explanation
In the first case, 
3
3 of the 
6
6 cells in the grid contain battleships. Therefore, the probability that your shot will hit one of them is 
3
/
6
=
0
.
5
3/6=0.5.
In the second case, all 
4
4 cells contain battleships, resulting in a probability of 
1
.
0
1.0 of hitting a battleship.
"""

from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  # count the no of 1's
  count = 0
  for li in G:
    for i in li:
      if i == 1:
        count += 1
  
  prob = format(count/(R * C), '.8f')
  
  return prob

# 1
R = 2
C = 3
G = [
  [0,0,1], 
  [1,0,1]   
     ]
print(getHitProbability(R, C, G))

# 2
R = 2
C = 2
G = [
  [1,1]
  [1,1]
  ]

print(getHitProbability(R, C, G))