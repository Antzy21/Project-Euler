from Problems import Problem2
from Problems import Problem3
from Problems import Problem4
from Problems import Problem5
from Problems import Problem6
from Problems import Problem7
from Problems import Problem8
from Problems import Problem9
from Problems import Problem11
from Problems import Problem12
from Problems import Problem13
from Problems import Problem14
from Problems import Problem15
from Problems import Problem16
from Problems import Problem17
from Problems import Problem18
from Problems import Problem19
from Problems import Problem20
from Problems import Problem21
from Problems import Problem22
from Problems import Problem23
from Problems import Problem24
from Problems import Problem67

from multiprocessing import Process, cpu_count
import time
import queue
from Functions.Divisors import getProperDivisors

def printSolver(func, i):
    result = func()
    print(f"Problem {i}: {result}")

problems = {
    2: Problem2.solve,
    3: Problem3.solve,
    4: Problem4.solve,
    5: Problem5.solve,
    6: Problem6.solve,
    7: Problem7.solve,
    8: Problem8.solve,
    9: Problem9.solve,
    11: Problem11.solve,
    12: Problem12.solve,
    13: Problem13.solve,
    14: Problem14.solve,
    15: Problem15.solve,
    16: Problem16.solve,
    17: Problem17.solve,
    18: Problem18.solve,
    19: Problem19.solve,
    20: Problem20.solve,
    21: Problem21.solve,
    22: Problem22.solve,
    23: Problem23.solve,
    24: Problem24.solve,
    67: Problem67.solve,
}

for problemNumber in problems:
    solveFunction = problems[problemNumber]
    printSolver(solveFunction, problemNumber)