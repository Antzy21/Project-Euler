from importlib import import_module
import time
import os

def printSolver(func, i):
    t1 = time.perf_counter()
    result = func()
    t2 = time.perf_counter()
    print(f"Problem {i:3}: {result:12} - {round(t2-t1,2)}s")

# Get all the problem solvers dynamically
for file in os.listdir("Problems"):
    
    if ".py" not in file:
        continue
    
    problemName = file.removesuffix(".py")
    problemNumber = int(problemName.removeprefix("Problem"))
    
    module = import_module(f"Problems.{problemName}")
    solveFunction = getattr(module, "solve")
    
    # Run the solve function
    printSolver(solveFunction, problemNumber)