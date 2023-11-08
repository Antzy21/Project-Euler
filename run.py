from importlib import import_module
import time
import os

def _printSolver_(func, i):
    t1 = time.perf_counter()
    result = func()
    t2 = time.perf_counter()
    print(f"Problem {i:3}: {result:12} - {round(t2-t1,2)}s")

def getProblemSolvers():
    problems = {}

    # Get all the problem solvers dynamically
    for file in os.listdir("Problems"):
        
        if ".py" not in file:
            continue
        
        problemName = file.removesuffix(".py")
        problemNumber = int(problemName.removeprefix("Problem"))
        
        module = import_module(f"Problems.{problemName}")
        solveFunction = getattr(module, "solve")
        
        problems[problemNumber] = solveFunction

    return problems

if __name__ == "__main__":
    
    problems = getProblemSolvers()

    for problemNumber in problems:
        solveFunction = problems[problemNumber]
        _printSolver_(solveFunction, problemNumber)
