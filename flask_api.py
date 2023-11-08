from flask import Flask, json
from importlib import import_module
from run import getProblemSolvers
import time
import os

api = Flask(__name__)

@api.route('/')
def index():
    return '<h1>Project Euler Solutions</h1>'

@api.route('/healthcheck', methods=['Get'])
def get_healthcheck():
    return json.dumps({
        "healthy": True
    })

@api.route('/solve/<numberStr>', methods=['Get'])
def solve(numberStr):
    try:
        number = int(numberStr)
    except:
        return(f"{numberStr} is not a number", 400)

    if number not in problems:
        return(f"No solution for {number}")

    solveFunction = problems[number]
    try:
        result = solveFunction()
    except:
        result = "Error"
    jsonObj = {
        "problem": number,
        "solution": result
    }

    return json.dumps(jsonObj)

if __name__ == "__main__":

    problems = getProblemSolvers()

    api.run(host ='0.0.0.0', port = 5000, debug = True)
