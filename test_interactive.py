""" File:test_interactive.py
    Author: Xin Li
    Purpose: additional test cases for pos interact
"""


import subprocess


input = """standard
-2 1
20 10
a b
0 0
1 2
1 3
1 1
5 5
0 2
5 2
4 2
2 2
3 2
4 5
3 5
6 5
8 3
2 4
8 1
6 8
1 8
9 2
9 1
9 5
9 4
9 3
7 5
8 5
1 6
1 5
1 7
6 9
7 8
8 8
5 8
"""



proc = subprocess.run(["python", "interactive.py"],
                      input = input.encode("utf-8"))

print()
print("---------------------------------------------------")
print("Testcase completed")
