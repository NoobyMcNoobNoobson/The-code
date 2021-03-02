import pandas as pd # this imports pandas like we need to
from pandas import DataFrame # i created a python virtual environment to use run pandas and it worked like a charm, I used tje pipenv command like the tutorial video that I sent you.

print ('pandas version: ' + pd.__version__) # I am using this to make sure I am in the right environment

#C:\\Users\\dhaka\\OneDrive\\Desktop\\Semester material\\Data Skills class\\All Homework\\three\\The-code

import os # to collect the files from the corresponding diretory 
from os import path # taking the right module from the library

def main(): # this connects all the other functions togethe
    the_size()

def the_size():
    data_sample = pd.read_csv("surveys.csv") # dear paul, this is one is designed to have the csv files in the corresponding directory.
    print('The shape of the surveys csv files is listed as follows :- ')
    print(data_sample.shape)

main()
    
    
