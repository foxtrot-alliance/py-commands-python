import re
import os
import sys
import csv
import time
import math
import random
import datetime
import traceback
import ctypes
import pywinauto
import keyboard
import openpyxl
import win32com
import win32gui
import win32timezone
import numpy
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import pandas
import requests
import xlrd
import xlwt
import pythoncom
from bs4 import BeautifulSoup


def retrieve_project_parameters():
    
    parameters = sys.argv

    parameters_number = parameters.index("-traces") if "-traces" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        traces = parameters[parameters_number]
    else:
        traces = ""

    parameters_number = parameters.index("-file") if "-file" in parameters else None
    if parameters_number is not None:
        parameters_number = parameters_number + 1
        file = parameters[parameters_number]
    else:
        file = ""
        
    return {
        "traces": traces,
        "file": file,
    }


def validate_project_parameters(parameters):
    
    traces = parameters["traces"]
    file = parameters["file"]
    
    if traces == "" or traces.upper() == "FALSE":
        traces = False
    elif traces.upper() == "TRUE":
        traces = True
    else:
        return "ERROR: Invalid traces parameter! Parameter = " + str(traces)

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved start * ===")

    if not file == "":
        if os.path.exists(file):
            if not file.upper().endswith(".PY") and not file.upper().endswith(".TXT"):
                return "ERROR: The file is not PY or TXT!"
        else:
            return "ERROR: The file was not found!"
    else:
        return "ERROR: The file parameter is empty!"

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "\tFile = " + str(file))

    if traces is True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Parameters retrieved end * ===")
        
    return {
        "traces": traces,
        "file": file,
    }
        
    
def execute_command(parameters):
    
    traces = parameters["traces"]
    file = parameters["file"]
    
    try:
        if traces is True:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform command start * ===")
            
        with open(file, "r") as f:
            code = f.read()
            
        exec(compile(code, '', 'exec'))
        
        code = None

        if traces is True:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + "=== * Perform command end * ===")
    
    except:
        print(traceback.format_exc())
        return "ERROR: Unexpected issue!"
    
    return True
    
    
def main():
    
    parameters = retrieve_project_parameters()
    
    parameters = validate_project_parameters(parameters)
    if not isinstance(parameters, dict):
        print(str(parameters))
        return
    
    valid = execute_command(parameters)
    if not valid is True:
        print(str(valid))
        return
    
    print("SUCCESS")
    
    
if __name__ == "__main__":
    main()
