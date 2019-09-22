# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/test',methods = ["GET"])
def test_api():
    return "API is working"


def calculate_mean(arr):
    mn=0
    for elem in arr:
        mn = mn+elem
    return (mn/len(arr))


@app.route('/std', methods = ['POST'])
def calculate_std():
    #{"arr":[200,12,12,122,134]} - json input
    print(json.loads(request.data.decode()))
    arr = json.loads(request.data.decode())['arr']
    print("The input is : ", arr)
    mn = calculate_mean(arr)
    std_dev = 0
    for elem in arr:
        std_dev = std_dev + (elem - mn)**2
    std_str = str(np.sqrt(std_dev/len(arr)))
    return std_str


if __name__ == '__main__':
    app.run()