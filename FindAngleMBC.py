""" 1BC is a right triangle, 90° at B.
Therefore, ABC = 90°.

Point MC is the midpoint of hypotenuse 1AC.

You are given the lengths AB and BC.
Your task is to find MBC (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints


Lengths AB and BC are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab, ac = map(int, open(0).readlines())
print(str(round(math.degrees(math.atan(ab/ac))))+chr(176))
