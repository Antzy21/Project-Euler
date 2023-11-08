from flask import Flask, json
from importlib import import_module
from run import getProblemSolvers
import time
import os

api = Flask(__name__)

@api.route('/')
def index():
    return '<h1>Hello World</h1>'

@api.route('/healthcheck', methods=['Get'])
def get_healthcheck():
    return json.dumps({
        "healthy": True
    })

@api.route('/problem/<numberStr>', methods=['Get'])
def get_solution(numberStr):
    number = int(numberStr)
    solveFunction = problems[number]
    result = solveFunction()
    jsonObj = {
        "problem": number,
        "solution": result
    }

    return json.dumps(jsonObj)

if __name__ == "__main__":

    problems = getProblemSolvers()

    api.run(host ='0.0.0.0', port = 5000, debug = True)
