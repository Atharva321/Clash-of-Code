"""
 In a climbing contest there is a number of problems (climbing routes) with varying difficulty. The contestants are free to chose which problems they want to attempt. Each problem is worth one millions points divided by the number of contestants that completes the problem, rounded to nearest integer.

Calculate the score of the winner of the contest.

Note: Round the score for each problem, not the end result.


Input
Line 1: An integer N for the number of problems
Line 2: An integer C for the number of contestants
Next C lines: A line for each contestant in order, starting with contestant 1. Each line is a string with a character for each problem, the character is an X if the problem is completed or an O if it is not.
Output
Line 1: The winning player and score separated with space
Constraints
1 ≤ N ≤ 100
1 ≤ C ≤ 100


Input

10
8
XXOOOXOOOO
XXOOXXXOOO
XOOXOOOOOO
XXXXOOOXOO
XXOXXOOOXX
XOXXOXOOXX
OXOXXOOXOX
OOOOOOOXXX

Output

2 2033333


"""
