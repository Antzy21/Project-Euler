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
from Problems import Problem67

def printSolver(func, i):
    result = func()
    print(f"Problem {i}: {result}")

printSolver(Problem11.solve, 11)
printSolver(Problem12.solve, 12)
printSolver(Problem13.solve, 13)
#solverHelper(Problem14.solve, 14)
#solverHelper(Problem15.solve, 15)
printSolver(Problem16.solve, 16)
printSolver(Problem17.solve, 17)
printSolver(Problem18.solve, 18)
printSolver(Problem19.solve, 19)
printSolver(Problem20.solve, 20)
printSolver(Problem21.solve, 21)
printSolver(Problem22.solve, 22)
printSolver(Problem67.solve, 67)