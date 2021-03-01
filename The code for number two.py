import pandas as pd
from pandas import DataFrame

print ('pandas version: ' + pd.__version__)

#C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\three\\The code\\The-code

import os
from os import path

def main():
    the_size()

def the_size():
    os.chdir('C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\three\\The code\\The-code')
    data_sample = pd.read_csv("surveys.csv")
    
    
